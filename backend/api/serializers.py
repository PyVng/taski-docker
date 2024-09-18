"""Serializers for the API module."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """A serializer for some model."""

    class Meta:
        """A serializer for some model."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
