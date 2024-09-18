"""Admin configuration for the API module."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Admin interface for the SomeModel."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
