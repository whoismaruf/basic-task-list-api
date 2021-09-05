from rest_framework import generics
from core.models import Task
from core.serializers import TaskSerializer
from root.permissions import TaskerPermission

# Create your views here.


class TaskView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Task.objects.all().filter(
            tasker=self.request.user
        ).order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = (TaskerPermission,)
    def perform_create(self, serializer):
        serializer.save(tasker=self.request.user)



class TaskRetriveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (TaskerPermission,)
