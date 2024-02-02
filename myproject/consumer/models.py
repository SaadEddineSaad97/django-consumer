from django.db import models
from django_celery_results.models import TaskResult


class CustomTaskResult(models.Model):
    task_result = models.OneToOneField(TaskResult, on_delete=models.CASCADE)
    additional_field = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"TaskResult - {self.task_result.id}"
