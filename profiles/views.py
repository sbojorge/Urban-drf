from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from .models import Profile
from .serializers import ProfileSerializer
from urban_drf.permissions import IsOwnerOrReadOnly


class ProfileList(ListAPIView):
    """
    Retrieves the list of existing profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(RetrieveUpdateAPIView):
    """
    Retrieves a single profile by its id and let the user make modifications to the profile
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]


