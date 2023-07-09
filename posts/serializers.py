from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Creates a serializer for the Post model
    """
    owner = serializers.CharField(read_only=True, source='owner.username') # Overrides the default owner's behavior
        
    class Meta:
        model = Post
        fields = '__all__'
    
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