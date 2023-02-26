from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from applications.product.models import Archive, Course, CourseItem, CourseItemFile
from applications.feedback.views import FeedbackMixin
from applications.product.permissions import IsFeedbackOwner, IsProductOwnerOrReadOnly, IsCourseItemOwner, IsCourseItemFileOwner
from applications.product.serializers import ArchiveSerailizer, CourseItemFileSerializer, CourseItemSerializer, ProductSerializer


class PaginationApiView(PageNumberPagination):
    page_size = 12
    max_page_size = 100
    page_size_query_param = 'courses'

class ProductViewSet(ModelViewSet, FeedbackMixin):
    serializer_class = ProductSerializer
    queryset = Course.objects.all()
    permission_classes = [IsProductOwnerOrReadOnly]
    
    pagination_class = PaginationApiView
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category__title', 'sub_category', 'title']
    search_fields = ['title', 'category__title', 'author__first_name']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_permissions(self):
        actions = ['delete_comment', 'update_comment', 'like', 'rating', 'add_comment', 'favourite']
        if self.action in actions:
            return [IsFeedbackOwner()]
        return super().get_permissions()
    
    
    
class ProductItemViewSet(ModelViewSet):
    serializer_class = CourseItemSerializer
    queryset = CourseItem.objects.all()
    permission_classes = [IsCourseItemOwner]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    
class ProductItemFileViewSet(ModelViewSet):
    serializer_class = CourseItemFileSerializer
    queryset = CourseItemFile.objects.all()
    permission_classes = [IsCourseItemFileOwner]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    
class ArchiveApiView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ArchiveSerailizer
    queryset = Archive.objects.all()
    permission_classes = [IsAuthenticated]