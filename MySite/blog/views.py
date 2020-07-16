from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
#from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
#from taggit.models import Tag
from django.db.models import Count




def home(request):
    """Renders the home page. Should this be on the project level?"""
    return render(request,'blog/index.html')


def post_list(request, tag_slug=None):
    """Displays the posts."""

    object_list = Post.objects.all()

    #tag = None

    #if tag_slug:
    #    tag = get_object_or_404(Tag, slug=tag_slug)
    #    object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3) # 3 posts per page
    page = request.GET.get('page') #what is this doing?
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer then deliver the first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If the page is out of range deliver the last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page,'posts': posts})
    #return render(request, 'blog/post/list.html', {'page': page,'posts': posts, 'tag': tag})


def post_detail(request, year, month, day, post):
    """Single Post"""

    post = get_object_or_404(Post, slug=post,                                  
                                   created__year=year, 
                                   created__month=month,
                                   created__day=day)


    return render(request, 'blog/post/detail.html',
                 {'post': post,})


def post_share(request, post_id):
    """Sharing a post via email. This view handles both the processing of get request and post."""
    post = get_object_or_404(Post, id=post_id)
    sent = False

    if request.method =='POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"Yo. {cd['name']} thinks you should read {post.title}"
            message = f"Read that shit at {post_url}"
            send_mail(subject, message, '153144green@chsbr.net', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})


