# from rest_framework.permissions import BasePermission


# class IsCurier(BasePermission):
#     def has_permission(self, request, view):
#         return bool(request.user.is_curier)
    

# class IsOwnerPersmission(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_authenticated and request.user.phone_number == obj.phone_sender

from rest_framework.permissions import BasePermission

class IsCourier(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_curier)

class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.phone_number == obj.phone_sender
