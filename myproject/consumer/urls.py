from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import process_message_view, TaskResultViewSet

router = DefaultRouter()
router.register(r'task-results', TaskResultViewSet, basename='task-result')

urlpatterns = [
    path('process-message/', process_message_view, name='process-message'),
    path('api/', include(router.urls)),
]
