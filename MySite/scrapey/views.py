from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .data import data_import
from .models import Post
from .scrapers import scrape_runner


print('http://127.0.0.1:8000/blog-external/')
# print('http://127.0.0.1:8000/blog-external/data')
print('http://127.0.0.1:8000/blog-external/my-api')
# scrape_runner.scrape_new_data()

from rest_framework import viewsets

from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def post_list(request):
    """Displays the posts."""

    blog_posts = Post.objects.all()

    paginator = Paginator(blog_posts, 7) 
    page = request.GET.get('page') 
   
    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer then deliver the first page.
        blog_posts = paginator.page(1)
    except EmptyPage:
        # If the page is out of range deliver the last page of results.
        blog_posts = paginator.page(paginator.num_pages)

    return render(request, 'scrapey/post/list.html', {'posts': blog_posts})




def post_detail(request, year, month, day, post):
    """Single Post"""

    # Below method raises an exception if the post is not found based on the url inputs provided.
    post = get_object_or_404(Post, slug=post,                                  
                                   date__year=year, 
                                   date__month=month,
                                   date__day=day)
    
    template_name = post.get_template_name()

    return render(request, 'scrapey/post/detail/' + template_name , {'post': post})



def data_play(request):
    """!!!"""
    
    if request.method == 'POST':
        #Depending on what button you click you will performa a different action

        button_value = request.POST.get('Button')
        
        if button_value == 'sql':            
            data_import.import_sql()        
            

    return render(request, 'scrapey/data.html')