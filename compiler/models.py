from django.db import models
from django.contrib.auth.models import User
import json

DIFFICULTY_CHOICES = [
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
]

LANGUAGE_CHOICES = (
    ('python', 'Python'),
    ('cpp', 'C++'),
)

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Problem statement only, no I/O or constraints here.")
    input_format = models.TextField(blank=True, null=True)
    output_format = models.TextField(blank=True, null=True)
    constraints = models.TextField(blank=True, null=True)
    sample_input = models.TextField(blank=True, null=True)
    sample_output = models.TextField(blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='test_cases')
    input_data = models.TextField()
    expected_output = models.TextField()

    def __str__(self):
        return f"TestCase for {self.problem.title}"


class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    verdict = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    detailed_verdicts = models.JSONField(default=list)  

    def __str__(self):
        return f"Submission by {self.user.username} for {self.problem.title}"