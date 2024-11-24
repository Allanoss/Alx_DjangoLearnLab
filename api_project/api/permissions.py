from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admins to modify data.
    """

    def has_permission(self, request, view):
        # Allow GET requests for everyone, but restrict other methods
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_staff