from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        print(request)
        print(view)
        print(obj)
        print(permissions.SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.album.user == request.user
