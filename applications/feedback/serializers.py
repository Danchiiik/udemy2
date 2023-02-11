from rest_framework import serializers
from applications.feedback.models import Comment, Favourite, Like, Rating
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Comment
        fields = '__all__'
        
        
class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='onwer.email')
    rating = serializers.IntegerField(min_value=1, max_value=10)
    
    class Meta:
        model = Rating
        fields = ['owner', 'rating']
        

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Like
        fields = '__all__'
     
        
class FavouriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Favourite
        fields = '__all__'
        