from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, filters
from .models import Post
from .serializers import PostSerializer
from urban_drf.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class PostListCreate(ListCreateAPIView):
    """
    Retrieves the list of existing posts and let the user create a new post
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count = Count('likes', distinct=True),
        comments_count = Count('comment', distinct=True)
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username', 'title'
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_on',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Retrieves a post by id and let the owner of the post to update/delet it
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count = Count('likes', distinct=True),
        comments_count = Count('comment', distinct=True)
    ).order_by('-created_on')
