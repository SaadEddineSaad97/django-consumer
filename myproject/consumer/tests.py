from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomTaskResult


class ProcessMessageViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_process_message_view(self):
        url = reverse('process-message')
        data_to_send = {'text': 'Test', 'timestamp': '2022-01-01T00:00:00Z', 'id': 5}

        response = self.client.post(url, data_to_send, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('task_id', response.json())

    def test_process_message_view_invalid_method(self):
        url = reverse('process-message')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.json())


class TaskResultViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_result = CustomTaskResult.objects.create(task_id='test_task_id', additional_field='test_result')

    def test_task_result_viewset_list(self):
        url = reverse('task-result-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_task_result_viewset_detail(self):
        url = reverse('task-result-detail', args=[self.task_result.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['task_id'], 'test_task_id')
        self.assertEqual(response.json()['additional_field'], 'test_result')
