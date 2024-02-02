from celery import shared_task
from django_celery_results.models import TaskResult
import requests

from myproject.myproject.configs import WebhookConfig


@shared_task
def process_message(message_data) -> str:
    """
    param: message_data : the data received from the producer
    return: Celery ID for the Task that was run

    This is a celery task process the received data, make a request to the specified webhook URL, and store the
    result in the Django database

    """
    webhook_url = WebhookConfig.webhook_url

    processed_text = message_data['text'][::-1]

    response = requests.post(webhook_url, json={'result': processed_text, 'message_id': message_data['id']})

    task_result = TaskResult.objects.create(
        task_id=process_message.request.id,
        result=response.text if response.ok else f"Failed with status code {response.status_code}",
    )

    return task_result.id
