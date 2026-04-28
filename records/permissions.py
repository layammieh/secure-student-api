from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin').exists()


class IsFaculty(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Faculty').exists()


class IsAdminOrFaculty(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(
            name__in=['Admin','Faculty']
        ).exists()