from rest_framework.permissions import BasePermission

class IsAdminToPost(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user and request.user.is_authenticated and request.user.is_staff
        return True
        
        