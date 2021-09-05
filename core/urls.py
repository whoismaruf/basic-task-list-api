from django.urls import path
from core.views import TaskView, TaskRetriveDestroyView


urlpatterns = [
    path(
        '',
        TaskView.as_view(),
        name='task-view'
    ),
    path('<int:pk>/', TaskRetriveDestroyView.as_view(), name='task_detail'),
]
