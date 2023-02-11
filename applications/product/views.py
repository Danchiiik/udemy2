from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# from applications.feedback.views import FeedbackMixin
from applications.product.models import Product
from applications.product.permissions import IsProductOwnerOrReadOnly


from applications.product.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsProductOwnerOrReadOnly]
    
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    
    # def get_permissions(self):
    #     if self.action == 'delete_comment':
    #         return [IsFeedbackOwner()]
    #     return super().get_permissions()