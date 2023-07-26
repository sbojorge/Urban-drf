from rest_framework import serializers
from likes.models import Like
from django.db import IntegrityError


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.CharField(
        read_only=True, source='owner.username')  # Overrides the default owner's behavior

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
