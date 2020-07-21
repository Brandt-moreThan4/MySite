from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='blog-home' ),
    path('blog/', views.post_list, name='post_list' ),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail' ),
    path('blog/<int:post_id>/share/', views.post_share, name='post_share'),
    path('books/', views.book_list, name='book_list'),
    
    ]