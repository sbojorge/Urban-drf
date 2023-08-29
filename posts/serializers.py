from rest_framework import serializers
from .models import Post
from likes.models import Like
from django_countries.serializers import CountryFieldMixin


class PostSerializer(CountryFieldMixin,serializers.ModelSerializer):
    """
    Creates a serializer for the Post model
    """
    owner = serializers.CharField(
        read_only=True, source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    like_id = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_is_owner(self, obj):
        request = self.context['request']
        if request.user == obj.owner:
            return True
        else:
            return False

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            print(like)
            return like.id if like else None
        return None

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

    # Validates the video size
    def validate_video(self, value):
        if value.size > 1024 * 1024 * 60:
            raise serializers.ValidationError(
                'Video size larger than 60 MB!'
            )
        return value
