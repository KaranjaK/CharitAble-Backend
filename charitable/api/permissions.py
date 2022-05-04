from rest_framework.permissions import BasePermission

class IsNgoUser(BasePermission):
    def has_permission(self, request, view):



        return bool(request.user and request.user.is_Ngo)
    

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):



        return bool(request.user and request.user.is_Admin)
    

class IsDonorUser(BasePermission):
    def has_permission(self, request, view):



        return bool(request.user and request.user.is_Donor)