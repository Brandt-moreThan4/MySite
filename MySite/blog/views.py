from django.shortcuts import render
from .models import Post


def post_list(request, tag_slug=None):
    """Displays the posts."""

    #post = Post.created_posts.all()
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

    #object_list = Post.published.all()
    #tag = None

    #if tag_slug:
    #    tag = get_object_or_404(Tag, slug=tag_slug)
    #    object_list = object_list.filter(tags__in=[tag])

    #paginator = Paginator(object_list, 3) # 3 posts per page
    #page = request.GET.get('page')
    #try:
    #    posts = paginator.page(page)
    #except PageNotAnInteger:
    #    posts = paginator.page(1)
    #except EmptyPage:
    #    posts = paginator.page(paginator.num_pages)

    #return render(request, 'blog/post/list.html', {'page': page,'posts': posts, 'tag': tag})


def post_detail(request, year, month, day, post):
    """Single Post"""

    post = get_object_or_404(Post, slug=post,                                  
                                   publish__year=year, 
                                   publish__month=month,
                                   publish__day=day)


    return render(request, 'blog/post/detail.html',
                 {'post': post,})