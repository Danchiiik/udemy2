from rest_framework import serializers
from django.db.models import Avg
from applications.feedback.models import Comment
from applications.feedback.serializers import CommentSerializer

from applications.product.models import Archive, Course, CourseItem, CourseItemFile

    
class CourseItemSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    files = serializers.ListField(
        child=serializers.FileField(max_length=None, allow_empty_file=False, use_url=False),
        min_length=5,
        max_length=None,
        write_only=True, 
    )
    
    class Meta:
        model = CourseItem
        fields = '__all__'    

    def create(self, validated_data):
        files_data = validated_data.pop("files")
        course_files = CourseItem.objects.create(**validated_data)
        for file in files_data:
            CourseItemFile.objects.create(course_item=course_files, files=file)
        
        return course_files
    
        
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
    