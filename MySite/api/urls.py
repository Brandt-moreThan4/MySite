from django.urls import path, include
from . import views
from rest_framework import routers

from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'api'

# router = routers.DefaultRouter()
# router.register(r'blog-external', views.PostViewSet, basename='blog-external')
# router.register(r'blogposts', views.BlogPostViewSet)

# urlpatterns = [

    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # ]

urlpatterns = [
    path('blog-posts/', views.blog_post_list)
    # path('blog-external/<int:pk>', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)