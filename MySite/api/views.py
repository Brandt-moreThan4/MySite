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



@api_view(['GET', 'POST'])
def blog_external_list(request, format=None):
    """
    List the top 10 external blog posts.  should update this to include the ability to filter by blog
     name as well.
    """

    

    if request.method == 'GET':
        query_set = Post.objects.all()

        # Filter by the url or title in the query string if one is given
        if request.GET.get('url'):
            query_set = query_set.filter(url=request.GET.get('url'))
        elif request.GET.get('title'):
            query_set = query_set.filter(title=request.GET.get('title'))
        
        if query_set:
            # If there is something in the query set then return it in the response.
            serializer = PostSerializer(query_set[0])
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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

