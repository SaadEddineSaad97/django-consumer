from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_results.models import TaskResult
import requests

from myproject.consumer.configs import WebhookConfig


@receiver(post_save, sender=TaskResult)
def send_result_to_producer(sender, instance, **kwargs):
    if kwargs.get('created', False):
        webhook_url = WebhookConfig.webhook_url
        response = requests.post(webhook_url, json={'result': instance.result, 'task_result_id': instance.id})
