from django.urls import path
from . import views

app_name = 'scrapey'

urlpatterns = [
    path('', views.post_list, name='post_list' ),
    path('data/', views.data_play, name='post_list' ),
    path('blog-external/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail' ),

    ]