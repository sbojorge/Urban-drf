from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Creates a serializer for the Post model
    """
    owner = serializers.CharField(read_only=True, source='owner.username') # Overrides the default owner's behavior
    is_owner = serializers.SerializerMethodField()
        
    class Meta:
        model = Post
        fields = '__all__'
    
    # Get the value of the is_owner field
    def get_is_owner(self, obj):
        request = self.context['request']
        if request.user == obj.owner:
            return True
        else:
            return False
    
    # Validates the image size and dimensions
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 10:
            raise serializers.ValidationError(
                'Image larger than 10 MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    