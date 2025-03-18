# ./backend/api/admin.py
"""File admin."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Class Task admin."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
