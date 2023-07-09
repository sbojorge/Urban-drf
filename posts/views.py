from rest_framework.generics import ListCreateAPIView
from .models import Post
from .serializers import PostSerializer


class PostListCreate(ListCreateAPIView):
    """
    Retrieves the list of existing posts and let the user create a new post
    """
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    