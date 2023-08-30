from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from urban_drf.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class ReviewListCreate(ListCreateAPIView):
    """
    Retrieves the list of existing reviews and let the authenticated
    user create a new review
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'service'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieves a review by id and let its owner update/delete it
    """
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
