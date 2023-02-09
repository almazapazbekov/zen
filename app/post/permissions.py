from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif bool(request.user and request.user.is_authenticated):
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif bool(
                request.user and request.user.is_authenticated and obj.author == request.user.author or request.user.is_staff):
            return True
