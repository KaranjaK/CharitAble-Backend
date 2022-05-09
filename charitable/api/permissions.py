from rest_framework.permissions import BasePermission

class IsNonGoUser(BasePermission):
    def has_permission(self, request, view):



        return bool(request.user and request.user.is_NonGo)
    

class IsAdministratorUser(BasePermission):
    def has_permission(self, request, view):



        return bool(request.user and request.user.is_administrator)
    

class IsDonUser(BasePermission):
    def has_permission(self, request, view):



        return bool(request.user and request.user.is_Don)