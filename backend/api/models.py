"""Models for the API module."""
from django.db import models


class Task(models.Model):
    """A model representing some entity."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
