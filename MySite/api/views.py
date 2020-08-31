from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import PostSerializer, BlogPostSerializer
from scrapey.models import Post
from blog.models import BlogPost

print('http://127.0.0.1:8000/api/blog-external-list/')
print('http://127.0.0.1:8000/api/blog-external-list/most_recent')



@api_view(['GET', 'POST'])
def blog_external_list(request, format=None):
    """
    List the top 10 external blog posts
    """
    if request.method == 'GET':
        blog_external_posts = Post.objects.all()[:10]
        serializer = PostSerializer(blog_external_posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def blog_external_most_recent(request, format=None):
    """
    List the most recent blog post
    """
    if request.method == 'GET':
        queryset = Post.objects.all()

        name = request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name).order_by('-date')[0]
        else:
            queryset = queryset.order_by('-date')[0]

        serializer = PostSerializer(queryset)

        return Response(serializer.data)





@api_view(['GET', 'POST'])
def blog_list(request, format=None):
    """
    List all of my blog posts.
    """
    if request.method == 'GET':
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostViewSet(viewsets.ModelViewSet):
#     # queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         queryset = Post.objects.all()
#         author = self.request.query_params.get('author', None)
#         if author is not None:
#             queryset = queryset.filter(author=author)
#         return queryset

#     @action(detail=False)
#     def most_recent_post(self, request):

#         queryset = Post.objects.all()

#         author = self.request.query_params.get('author', None)
#         if author is not None:
#             queryset = queryset.filter(author=author).order_by('-date')[0]
#         else:
#             queryset = queryset.order_by('-date')[0]

#         serializer = self.get_serializer(queryset)

#         return Response(serializer.data)



# class BlogPostList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """

#     def get(self, request, format=None):
#         blog_posts = BlogPost.objects.all()
#         serializer = BlogPostSerializer(blog_posts, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = BlogPostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)