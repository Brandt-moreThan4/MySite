from django.urls import path, include
from . import views
from rest_framework import routers
# from blog.models import BlogPost

app_name = 'scrapey'

urlpatterns = [
    path('data/', views.data_play, name='post_list' ),
    path('blog-external/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail' ),
    ]
