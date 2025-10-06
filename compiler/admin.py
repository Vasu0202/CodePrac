from django.contrib import admin
from .models import Problem, TestCase, Submission


class TestCaseInline(admin.TabularInline):
    model = TestCase
    extra = 1


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'tags')
    list_filter = ('difficulty',)
    search_fields = ('title', 'description', 'tags')
    inlines = [TestCaseInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'difficulty', 'tags')
        }),
        ('Problem Details', {
            'fields': ('input_format', 'output_format', 'constraints', 'sample_input', 'sample_output', 'explanation')
        }),
    )


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('problem', 'user', 'language', 'verdict', 'created_at')
    list_filter = ('verdict', 'language')
    search_fields = ('code', 'user__username')
