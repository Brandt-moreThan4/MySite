from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.post_list, name='post_list' ),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail' ),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:year>/<int:month>/<int:day>/<slug:post>/', views.book_detail, name='book_detail'),
    path('knowledge-repo/', views.knowledge_repo,  name='knowledge_repo'),
    path('Questions/', views.question, name='questions'),
    path('', views.home, name='blog-home' ),
    ]