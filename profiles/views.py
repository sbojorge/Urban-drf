from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from .models import Profile
from .serializers import ProfileSerializer
from urban_drf.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ProfileList(ListAPIView):
    """
    Retrieves the list of existing profiles
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True)
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
         'owner__following__followed__profile',
         'owner__followed__owner__profile'
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__followed__created_on',
        'owner__following__created_on',
    ]


class ProfileDetail(RetrieveUpdateAPIView):
    """
    Retrieves a single profile by its id and let the user make modifications to the profile
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True)
    ).order_by('-created_on')
