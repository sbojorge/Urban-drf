from rest_framework import serializers
from .models import Review
from django.contrib.humanize.templatetags.humanize import naturaltime


class ReviewSerializer(serializers.ModelSerializer):
    """
    Creates a serializer for the Review model
    Adds extra fields when returning a list of review instances
    """
    owner = serializers.CharField(read_only=True, source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    is_owner = serializers.SerializerMethodField()
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    # Get the value of the is_owner field
    def get_is_owner(self, obj):
        request = self.context['request']
        if request.user == obj.owner:
            return True
        else:
            return False

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)


class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for the Review model used in detail view
    Automatically references the Service Id which the review is associated with
    """
    service = serializers.ReadOnlyField(source='service.id')
