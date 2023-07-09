from rest_framework.generics import ListAPIView
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(ListAPIView):
    """
    Retrieves the list of existing profiles
    """
    model = Profile
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
