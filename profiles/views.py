from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from .models import Profile
from .serializers import ProfileSerializer
from urban_drf.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from rest_framework import filters


class ProfileList(ListAPIView):
    """
    Retrieves the list of existing profiles
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count = Count('owner__post', distinct=True)
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'posts_count'
    ]
    

class ProfileDetail(RetrieveUpdateAPIView):
    """
    Retrieves a single profile by its id and let the user make modifications to the profile
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count = Count('owner__post', distinct=True)
    ).order_by('-created_on')
    


