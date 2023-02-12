from rest_framework import serializers
from django.db.models import Avg
from applications.feedback.models import Comment
from applications.feedback.serializers import CommentSerializer

from applications.product.models import Course

class ProductSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    
    class Meta:
        model = Course
        fields = '__all__'
        
        
    def create(self, validated_data):
        # request = self.context.get('request')
        product = Course.objects.create(**validated_data)
        return product
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        comment = Comment.objects.filter(product=instance.id)
        serializer = CommentSerializer(comment, many=True)
        comments = serializer.data
        
        rep['likes'] = instance.likes.filter(like=True).count()
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        rep['comment'] = comments
        return rep
    