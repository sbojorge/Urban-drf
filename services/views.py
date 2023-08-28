from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Service
from .serializers import ServiceSerializer
from urban_drf.permissions import IsOwnerOrReadOnly


class ServiceListCreate(ListCreateAPIView):
    """
    Retrieves the list of existing services and let the user create a new service
    """
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ServiceDetailList(RetrieveUpdateDestroyAPIView):
    """
    Retrieves a service by id and let the owner of the service to update/delet it
    """
    serializer_class = ServiceSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Service.objects.all()