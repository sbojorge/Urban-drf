from rest_framework import serializers
from .models import Service
from django_countries.serializers import CountryFieldMixin


class ServiceSerializer(CountryFieldMixin, serializers.ModelSerializer):
    """
    Creates a serializer for the Profile model
    """
    owner = serializers.CharField(read_only=True, source='owner.username')
    is_owner = serializers.SerializerMethodField()
    
    class Meta:
        model = Service
        fields = '__all__'


    def get_is_owner(self, obj):
        request = self.context['request']
        if request.user == obj.owner:
            return True
        else:
            return False
