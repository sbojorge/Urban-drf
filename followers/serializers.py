from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model
    """
    owner = serializers.CharField(
        read_only=True, source='owner.username')
    followed_name = serializers.CharField(
        read_only=True, source='followed.username')

    class Meta:
        model = Follower
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
