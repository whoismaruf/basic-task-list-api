from rest_framework import permissions


class TaskerPermission(permissions.BasePermission):
    """
        Default permissions for Blog API.
    """
    def has_object_permission(self, request, view, obj):
        # If you want user to GET other's tasks
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return obj.tasker == request.user
