# TODO здесь производится настройка пермишенов для нашего проекта

from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    message = 'Action allowed only for author'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
