from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from urban_drf.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CommentListCreate(ListCreateAPIView):
    """
    Retrieves the list of existing comments and let the authenticated
    user create a new comment
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'post'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieves a post by id and let the owner of the post to update/delet it
    """
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
