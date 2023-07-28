from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model

    """
    owner = serializers.CharField(read_only=True, source='owner.username') # Overrides the default owner's behavior
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_created_on(self, obj):
        
        return naturaltime(obj.created_on)

    def get_updated_at(self, obj):
        
        return naturaltime(obj.updated_on)

    class Meta:
        
        model = Contact
        fields = '__all__'