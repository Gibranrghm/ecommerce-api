from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only the owner of a product can edit/delete it.
    Everyone else can only read (GET).
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions (GET, HEAD, OPTIONS) are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions only allowed to the owner
        return obj.owner == request.user