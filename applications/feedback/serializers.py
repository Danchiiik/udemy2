from rest_framework import serializers
from applications.feedback.models import Comment, Favourite, Like, LikeComment, Rating
from django.contrib.auth import get_user_model

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
        rep['rating'] = float(Rating.objects.get(product_id=instance.product.id).rating)
        rep['review'] = Comment.objects.filter(product_id=instance.product.id).count()
        rep['price'] = f'{int(instance.product.price)} {instance.product.currency}' 
        
        return rep

