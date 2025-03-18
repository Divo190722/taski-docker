# ./backen/api/serializers.py
"""Serializers api."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Class serializer Task."""

    class Meta:
        """Class Meta."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
