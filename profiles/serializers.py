from rest_framework import serializers
from .models import Profile
from followers.models import Follower
from django_countries.serializers import CountryFieldMixin


class ProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    """
    Creates a serializer for the Profile model
    """
    owner = serializers.CharField(read_only=True, source='owner.username') # Overrides the default owner's behaviour
    is_owner = serializers.SerializerMethodField() # Add the is_owner field and its value to the serialized profile object
    posts_count = serializers.ReadOnlyField()
    following_id = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = '__all__'
    
    # Get the value of the is_owner field
    def get_is_owner(self, obj):
        request = self.context['request']
        if request.user == obj.owner:
            return True
        else:
            return False
    

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            # print(following)
            return following.id if following else None
        return None