from rest_framework import serializers
from .models import CustomTaskResult


class CustomTaskResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomTaskResult
        fields = '__all__'
