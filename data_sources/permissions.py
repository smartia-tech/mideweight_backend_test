from rest_framework import permissions
from django.conf import settings


class HasAPIAccess(permissions.BasePermission):
    message = 'Invalid or missing API Key.'

    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_AUTHORIZATION', '')
        if not api_key:
            return False
        try:
            return api_key == settings.SMARTIA_API_KEY.split('Bearer ')[1]
        except IndexError:
            return False
