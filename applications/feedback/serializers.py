from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Avg

from applications.feedback.models import Comment, Favourite, Like, LikeComment, Rating

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Comment
        fields = '__all__'
        
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = instance.likes_com.filter(like=True).count()
        return rep
        
        
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
     

class LikeCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = LikeComment
        fields = '__all__'
        

        
class FavouriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Favourite
        fields = '__all__'
    
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['image'] = str(instance.product.image)
        rep['title'] = instance.product.title
        rep['mentor'] = instance.product.author.first_name
        try:
            rep['rating'] = round(Rating.objects.filter(product_id=instance.product.id).aggregate(Avg('rating'))['rating__avg'], 1)
        except:
            rep['rating'] = None 
        rep['review'] = Comment.objects.filter(product_id=instance.product.id).count()
        rep['price'] = f'{int(instance.product.price)} {instance.product.currency}' 
        
        return rep
