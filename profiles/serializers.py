from rest_framework import serializers
from .models import Profile
from django_countries.serializers import CountryFieldMixin


class ProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    """
    Creates a serializer for the Profile model
    """
    owner = serializers.CharField(read_only=True, source='owner.username') # Overrides the default owner's behaviour
    
    class Meta:
        model = Profile
        fields = '__all__'