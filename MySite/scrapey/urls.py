from django.urls import path, include
from . import views
from rest_framework import routers
# from blog.models import BlogPost

app_name = 'scrapey'

urlpatterns = [

    path('', views.post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail' ),
    ]
