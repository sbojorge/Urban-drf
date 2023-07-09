from rest_framework import permissions

# This code comes from https://www.django-rest-framework.org/api-guide/permissions/#api-reference
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user