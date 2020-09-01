from django.urls import path, include
from . import views
from rest_framework import routers

from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'api'

# router = routers.DefaultRouter()
# router.register(r'blog-external', views.PostViewSet, basename='blog-external')
# router.register(r'blogposts', views.BlogPostViewSet)

urlpatterns = [
    path('blog-list/', views.blog_list),
    path('blog-external-list/', views.blog_external_list),
    path('blog-external-list/most-recent/', views.blog_external_most_recent)
]

urlpatterns = format_suffix_patterns(urlpatterns)

# urlpatterns = [
#     path('blog-posts/', views.BlogPostList.as_view()),
#     path('blog-posts/most_recent_post', views.BlogPostList.as_view())
# ]