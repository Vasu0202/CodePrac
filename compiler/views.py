import os
import uuid
import subprocess
import tempfile
import markdown
import shutil
import re

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView

from .models import Problem, TestCase, Submission
from .forms import StyledUserCreationForm, StyledAuthenticationForm


# ----------------- Utility Functions -----------------



def clean_output(output, max_length=10000):
    """Clean and truncate output to prevent oversized responses"""
    if len(output) > max_length:
        return output[:max_length] + f"\n...[Output truncated, too long. Max: {max_length} characters]"
    return output


def normalize_output(output: str) -> str:
    """
    Normalize spaces, brackets, commas, and casing for lenient comparison.
    Ensures [0,1], 0, 1, '0 1', ' 0   1' all match correctly.
    """
    if output is None:
        return ""
    s = str(output).strip().lower()
    # Replace brackets and commas with spaces
    s = re.sub(r'[\[\],]+', ' ', s)
    # Normalize multiple spaces and newlines
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


def outputs_match(user_output, expected_output):
    """Return True if user output logically matches expected output."""
    return normalize_output(user_output) == normalize_output(expected_output)


def run_docker_container(cmd, input_data, timeout):
    """Run Docker container with proper resource limits"""
    try:
        result = subprocess.run(
            cmd,
            input=input_data.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout
        )
        return result
    except subprocess.TimeoutExpired:
        raise
    except Exception as e:
        raise Exception(f"Docker execution failed: {str(e)}")


# ----------------- Code Execution API -----------------

class CodeCompileView(APIView):
    def post(self, request):
        code = request.data.get("code")
        language = request.data.get("language")
        input_text = request.data.get("input", "")

        if not code or not language:
            return Response({"error": "Both 'code' and 'language' are required."}, status=400)

        if len(code) > 10000:
            return Response({"error": "Code too long. Maximum 10000 characters allowed."}, status=400)

        uid = str(uuid.uuid4())
        base_path = os.path.join(tempfile.gettempdir(), uid)
        os.makedirs(base_path, exist_ok=True)

        try:
            docker_config = getattr(settings, 'DOCKER_CONFIG', {})
            memory_limit = docker_config.get('MEMORY_LIMIT', '256m')
            cpu_limit = docker_config.get('CPU_LIMIT', '1')
            timeout_seconds = docker_config.get('TIMEOUT_COMPILE', 30)

            if language == "python":
                file_path = os.path.join(base_path, "main.py")
                with open(file_path, "w") as f:
                    f.write(code)
                cmd = [
                    "docker", "run", "--rm",
                    f"--memory={memory_limit}",
                    f"--cpus={cpu_limit}",
                    "--network=none",
                    "-v", f"{base_path}:/app",
                    "-w", "/app",
                    "python:3.9-slim",
                    "python", "-u", "main.py"
                ]
            elif language == "cpp":
                file_path = os.path.join(base_path, "main.cpp")
                with open(file_path, "w") as f:
                    f.write(code)
                cmd = [
                    "docker", "run", "--rm",
                    f"--memory={memory_limit}",
                    f"--cpus={cpu_limit}",
                    "--network=none",
                    "-v", f"{base_path}:/app",
                    "-w", "/app",
                    "gcc:latest",
                    "bash", "-c",
                    "g++ -std=c++11 -O2 main.cpp -o main && ./main || echo 'Compilation failed'"
                ]
            else:
                return Response({"error": "Invalid language. Use 'python' or 'cpp'."}, status=400)

            result = run_docker_container(cmd, input_text, timeout_seconds)
            output = clean_output(result.stdout.decode())
            error = clean_output(result.stderr.decode())

            return Response({
                "output": output,
                "error": error,
                "return_code": result.returncode
            })

        except subprocess.TimeoutExpired:
            return Response({"error": f"Execution timed out ({timeout_seconds}s limit)."}, status=408)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        finally:
            shutil.rmtree(base_path, ignore_errors=True)


# ----------------- Code Submission API -----------------

class CodeSubmissionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        code = request.data.get("code")
        language = request.data.get("language")
        problem_id = request.data.get("problem_id")

        if not code or not language or not problem_id:
            return Response({"error": "code, language, and problem_id are required"}, status=400)

        if len(code) > 10000:
            return Response({"error": "Code too long. Maximum 10000 characters allowed."}, status=400)

        try:
            problem = Problem.objects.get(id=problem_id)
            test_cases = problem.test_cases.all()
        except Problem.DoesNotExist:
            return Response({"error": "Problem not found"}, status=404)

        uid = str(uuid.uuid4())
        base_path = os.path.join(tempfile.gettempdir(), uid)
        os.makedirs(base_path, exist_ok=True)

        try:
            docker_config = getattr(settings, 'DOCKER_CONFIG', {})
            memory_limit = docker_config.get('MEMORY_LIMIT', '256m')
            cpu_limit = docker_config.get('CPU_LIMIT', '1')
            timeout_seconds = docker_config.get('TIMEOUT_SUBMISSION', 15)

            if language == "python":
                file_path = os.path.join(base_path, "main.py")
                with open(file_path, "w") as f:
                    f.write(code)
                docker_cmd = [
                    "docker", "run", "--rm",
                    f"--memory={memory_limit}",
                    f"--cpus={cpu_limit}",
                    "--network=none",
                    "-v", f"{base_path}:/app",
                    "-w", "/app",
                    "python:3.9-slim",
                    "python", "-u", "main.py"
                ]
            elif language == "cpp":
                file_path = os.path.join(base_path, "main.cpp")
                with open(file_path, "w") as f:
                    f.write(code)
                docker_cmd = [
                    "docker", "run", "--rm",
                    f"--memory={memory_limit}",
                    f"--cpus={cpu_limit}",
                    "--network=none",
                    "-v", f"{base_path}:/app",
                    "-w", "/app",
                    "gcc:latest",
                    "bash", "-c",
                    "g++ -std=c++11 -O2 main.cpp -o main && ./main || echo 'Compilation failed'"
                ]
            else:
                return Response({"error": "Invalid language"}, status=400)

            verdicts = []
            passed_count = 0

            for i, tc in enumerate(test_cases):
                input_txt = tc.input_data.strip()
                expected_output = tc.expected_output.strip()

                try:
                    result = run_docker_container(docker_cmd, input_txt, timeout_seconds)

                    actual_output = result.stdout.decode().strip()
                    stderr_output = result.stderr.decode().strip()

                    if stderr_output and "Compilation failed" in stderr_output:
                        verdicts.append(f"Compilation Error (Test {i+1})")
                    elif stderr_output:
                        verdicts.append(f"Runtime Error (Test {i+1}): {clean_output(stderr_output, 500)}")
                    elif outputs_match(actual_output, expected_output):
                        verdicts.append(f"Accepted (Test {i+1})")
                        passed_count += 1
                    else:
                        verdicts.append(f"Wrong Answer (Test {i+1})")

                except subprocess.TimeoutExpired:
                    verdicts.append(f"Time Limit Exceeded (Test {i+1})")
                except Exception as e:
                    verdicts.append(f"System Error (Test {i+1}): {str(e)}")

            final_verdict = "Accepted" if passed_count == len(test_cases) else "Failed"

            Submission.objects.create(
                problem=problem,
                code=code,
                language=language,
                verdict=final_verdict,
                user=request.user,
                detailed_verdicts=verdicts
            )

            return Response({
                "verdicts": verdicts,
                "final_verdict": final_verdict,
                "passed": passed_count,
                "total": len(test_cases),
                "problem_title": problem.title
            })

        except Exception as e:
            return Response({"error": f"Submission failed: {str(e)}"}, status=500)
        finally:
            shutil.rmtree(base_path, ignore_errors=True)


# ----------------- Frontend Views -----------------

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = StyledUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('problem_list')
    else:
        form = StyledUserCreationForm()
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    authentication_form = StyledAuthenticationForm
    template_name = 'login.html'


@login_required
def problem_list(request):
    difficulty = request.GET.get('difficulty')
    problems = Problem.objects.all()
    if difficulty:
        problems = problems.filter(difficulty__iexact=difficulty)
    submissions = Submission.objects.filter(user=request.user)
    solved_ids = submissions.filter(verdict="Accepted").values_list('problem_id', flat=True).distinct()
    return render(request, 'judge/problem_list.html', {
        'problems': problems,
        'solved_ids': set(solved_ids),
        'selected_difficulty': difficulty,
    })


@login_required
def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    problem.description_html = markdown.markdown(problem.description or '', extensions=['extra'])
    problem.input_format_html = markdown.markdown(problem.input_format or '', extensions=['extra'])
    problem.output_format_html = markdown.markdown(problem.output_format or '', extensions=['extra'])
    problem.constraints_html = markdown.markdown(problem.constraints or '', extensions=['extra'])
    problem.sample_input_html = markdown.markdown(problem.sample_input or '', extensions=['extra'])
    problem.sample_output_html = markdown.markdown(problem.sample_output or '', extensions=['extra'])
    problem.explanation_html = markdown.markdown(problem.explanation or '', extensions=['extra'])
    return render(request, 'judge/problem_detail.html', {'problem': problem})


@login_required
def submissions_list(request):
    submissions = Submission.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'judge/submissions.html', {'submissions': submissions})


@login_required
def profile_view(request):
    total_submissions = Submission.objects.filter(user=request.user).count()
    accepted = Submission.objects.filter(user=request.user, verdict='Accepted').count()
    failed = total_submissions - accepted
    problems_solved = Submission.objects.filter(user=request.user, verdict='Accepted').values('problem').distinct().count()
    return render(request, 'judge/profile.html', {
        'user': request.user,
        'total_submissions': total_submissions,
        'accepted': accepted,
        'failed': failed,
        'problems_solved': problems_solved
    })
