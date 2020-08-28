from rest_framework import viewsets
from .serializers import PostSerializer
from scrapey.models import Post

print('http://127.0.0.1:8000/api')

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


