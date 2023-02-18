from rest_framework.permissions import BasePermission, SAFE_METHODS

from applications.feedback.models import Comment
from applications.product.models import Course, CourseItem
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.response import Response


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
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            if request.method == 'POST':
                return request.user.is_authenticated and request.user.is_mentor and (request.data['email'] == Course.objects.get(id=request.data['product']).author.email)
        except MultiValueDictKeyError:
            return Response('field "title" and "product" is required')
        except:
            return 'Something went wrong'
            
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated or request.user.is_staff
        return request.user.is_authenticated and (request.user == obj.author)
    

class IsCourseItemFileOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            if request.method == 'POST':
                print(request.data)
                return request.user.is_authenticated and request.user.is_mentor and (request.data['email'] == CourseItem.objects.get(id=request.data['course_item']).author.email)
        except MultiValueDictKeyError:
            return Response('field "title" and "product" is required')
        except:
            return 'Something went wrong'
            
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
