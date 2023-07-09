from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from urban_drf.permissions import IsOwnerOrReadOnly


class PostListCreate(ListCreateAPIView):
    """
    Retrieves the list of existing posts and let the user create a new post
    """
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class PostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Retrieves a post by id and let the owner of the post to update/delet it
    """
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    