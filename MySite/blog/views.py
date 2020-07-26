from django.shortcuts import render, get_object_or_404
from .models import Post, Book, Comment, Knowledge
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from taggit.models import Tag
#from django.db.models import Count
from django.db.models import Q



def home(request):
    """Renders the home page. """


    return render(request,'blog/index.html')


def post_list(request, tag_slug=None):
    """Displays the posts."""

    object_list = Post.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 6) 
    page = request.GET.get('page') #what is this doing?
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer then deliver the first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If the page is out of range deliver the last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page,'posts': posts, 'tag': tag})


def post_detail(request, year, month, day, post):
    """Single Post"""

    # Below method raises an exception if the post is not found based on the url inputs provided.
    post = get_object_or_404(Post, slug=post,                                  
                                   created__year=year, 
                                   created__month=month,
                                   created__day=day)

    # List of active comments for this post
    comments = post.comments.filter(active=True) 
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create comment object but don't commit it to the database yet so you can link it to the post
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html',
                 {'post': post,
                 'comments': comments,
                 'new_comment': new_comment,
                 'comment_form': comment_form})


def post_share(request, post_id):
    """Sharing a post via email. This view handles both the processing of get request and post.
    Currently there is no link on blog detail page to get to this. Need to fiddle with email stuff more first."""

    post = get_object_or_404(Post, id=post_id)
    sent = False

    if request.method =='POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"Yo. {form_data['name']} thinks you should read this post: {post.title}"
            message = f"Read that shit at {post_url} \n\n My comments: {form_data['comments']}" # I have not tested after adding this line yet
            send_mail(subject, message, 'brandtgreen97@gmail.com', [form_data['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})



def book_list(request):
    """Renders the generic book list view"""

    books = Book.objects.all()    

    return render(request, 'blog/book/list.html', {'books': books})


def book_detail(request):
    pass


def knowledge_repo(request):
    """Produces the beautiful table of learning"""

    try:
        search_term = request.GET['search_box']
    except:
        search_term = ''

    if search_term == '':
        knowledge_list = Knowledge.objects.all()
    else:
        #Does not filter for tags that well. I shoudl change the tags back to strings
        knowledge_list = Knowledge.objects.filter(Q(author__icontains=search_term) | Q(description__icontains=search_term) | Q(tags__name__in=[search_term]))

    return render(request, 'blog/knowledge_repo.html', {'knowledge_list': knowledge_list})


def data_import(request):
    """lolol"""
    
    #if request.method == 'POST':
    #    file = request.FILES['filey_name']
    #    for line in open(file):
    #        print(line)    
    #    print('lol')
    #try:
    #    input_value = request.GET['texty']
    #except:
    #    return render(request, 'blog/data_import.html')
    #else:
    #    return render(request, 'blog/data_import.html')
    return render(request, 'blog/data_import.html')

