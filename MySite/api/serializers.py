from scrapey.models import Post
from blog.models import BlogPost
from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id','post_title', 'created', 'post_body', 'slug']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'body','date','author','url','website','name']


# class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = BlogPost
#         fields = ['id','post_title', 'created', 'post_body']
