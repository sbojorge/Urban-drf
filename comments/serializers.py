from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Creates a serializer for the Comment model
    Adds extra fields when returning a list of comment instances
    """
    owner = serializers.CharField(read_only=True, source='owner.username') # Overrides the default owner's behavior
    profile_id = serializers.CharField(read_only=True, source='owner.profile.id')
    profile_image = serializers.CharField(read_only=True, source='owner.profile.image.url')
    is_owner = serializers.SerializerMethodField()
        
    class Meta:
        model = Comment
        fields = '__all__'
    
    # Get the value of the is_owner field
    def get_is_owner(self, obj):
        request = self.context['request']
        if request.user == obj.owner:
            return True
        else:
            return False

class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in detail view
    Automatically references the Post Id which the comment is associated with
    """
    post = serializers.CharField(read_only=True, source='post.id')
