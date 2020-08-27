from django.urls import path, include
from . import views
from rest_framework import routers
# from blog.models import BlogPost

app_name = 'scrapey'

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', views.post_list, name='post_list' ),
    path('my-api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('data/', views.data_play, name='post_list' ),
    path('blog-external/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail' ),

    ]
