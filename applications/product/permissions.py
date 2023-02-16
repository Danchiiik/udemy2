from rest_framework.permissions import BasePermission, SAFE_METHODS

from applications.feedback.models import Comment
from applications.product.models import Course


class IsProductOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated and request.user.is_mentor
        return request.user.is_authenticated and request.user == Course.objects.get(id=view.kwargs['pk']).author
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated or request.user.is_staff
        return request.user.is_authenticated and (request.user == obj.author)


class IsCourseItemOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated or request.user.is_staff
        return request.user.is_authenticated and (request.user == obj.author)

    
class IsFeedbackOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        try:
            return request.user.is_authenticated and request.user == Comment.objects.get(id=view.kwargs['pk']).owner
        except:
            return 'Something went wrong'
