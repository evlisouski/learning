from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # если метод (запрос) безопасный, то доступ есть у всех
        if request.method in permissions.SAFE_METHODS:
            return True

        # Иначе только администратор
        return bool(request.user and request.user.is_staff)


# Разрешение на уровне объекта
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        # сравниваем пользователя с тем пользователем, который пришел по запросу
        return obj.user == request.user
