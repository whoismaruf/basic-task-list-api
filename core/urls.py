from django.urls import path
from core.views import TaskView


urlpatterns = [
    path(
        '',
        TaskView,
        name='task'
    ),
]
