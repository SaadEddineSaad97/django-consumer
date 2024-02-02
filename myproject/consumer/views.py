# consumer/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .tasks import process_message  # Import your Celery task here


@csrf_protect
def process_message_view(request):
    if request.method == 'POST':
        data = request.json

        celery_task_result = process_message.delay(data)

        response_data = {'task_id': celery_task_result.id}
        return JsonResponse(response_data, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
