from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
from .models import Comment, RatingUser

class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = ['id', 'order', 'author', 'body', 'created_at']
    
    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment
    

class RatingSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = RatingUser
        fields = ['id', 'author', 'user', 'rating']
    
    def create(self, validated_data):
        user = self.context.get('request').user
        rating = RatingUser.objects.create(author=user, **validated_data)
        return rating
    
    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise ValidationError('Rating must be in range 1 - 5')
        return rating
