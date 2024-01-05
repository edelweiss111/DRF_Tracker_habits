from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Является ли пользователь владельцем"""
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
