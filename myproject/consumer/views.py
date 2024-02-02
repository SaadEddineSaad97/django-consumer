# consumer/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import CustomTaskResult
from .serializers import CustomTaskResultSerializer
from .tasks import process_message  # Import your Celery task here


@csrf_protect
def process_message_view(request):
    if request.method == 'POST':
        data = request.json

        celery_task_result = process_message.delay(data)

        response_data = {'task_id': celery_task_result.id}
        return JsonResponse(response_data, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


class TaskResultViewSet(viewsets.ModelViewSet):
    queryset = CustomTaskResult.objects.all()
    serializer_class = CustomTaskResultSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
