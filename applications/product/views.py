from rest_framework.viewsets import ModelViewSet
from applications.feedback.views import FeedbackMixin
from applications.product.models import Archive, Course, CourseItem, CourseItemFile
from applications.product.permissions import IsFeedbackOwner, IsProductOwnerOrReadOnly, IsCourseItemOwner
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.permissions import IsAuthenticated


from applications.product.serializers import ArchiveSerailizer, CourseItemFileSerializer, CourseItemSerializer, ProductSerializer


class ProductViewSet(ModelViewSet, FeedbackMixin):
    serializer_class = ProductSerializer
    queryset = Course.objects.all()
    permission_classes = [IsProductOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_permissions(self):
        actions = ['delete_comment', 'like', 'rating', 'add_comment', 'favourite']
        if self.action in actions:
            return [IsFeedbackOwner()]
        return super().get_permissions()
    
    
class ProductItemViewSet(ModelViewSet):
    serializer_class = CourseItemSerializer
    queryset = CourseItem.objects.all()
    permission_classes = [IsCourseItemOwner]

    def perform_create(self, serializer):
        user = self.request.user
        course_id = self.request.data['product'].author
        course = Course.objects.get(id=course_id, owner=user)
        serializer.save(course=course, owner=user)
    
class ProductItemFileViewSet(ModelViewSet):
    serializer_class = CourseItemFileSerializer
    queryset = CourseItemFile.objects.all()
    permission_classes = [IsCourseItemOwner]
    
    
class ArchiveApiView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ArchiveSerailizer
    queryset = Archive.objects.all()
    permission_classes = [IsAuthenticated]