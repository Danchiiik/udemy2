from rest_framework import serializers
from django.db.models import Avg
from applications.feedback.models import Comment
from applications.feedback.serializers import CommentSerializer

from applications.product.models import Archive, Course, CourseItem, CourseItemFile

    
class CourseItemSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model = CourseItem
        fields = '__all__'
        
    
class CourseItemFileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model = CourseItemFile
        fields = '__all__'    


class ArchiveSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    description = serializers.CharField(min_length=200)
    
    course_items = CourseItemSerializer(many=True, read_only=True)
    course_items_files = CourseItemFileSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = '__all__'
        
        
    def create(self, validated_data):
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
    