from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsRatingUser(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: User):
        return (obj.user == req.user)
