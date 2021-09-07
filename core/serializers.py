from django.db import models
from django.db.models import fields
from rest_framework import serializers
from core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    tasker = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Task
        fields = ('pk', 'name', 'created_at', 'tasker')
