from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Book, Comment, Knowledge, Question
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Q
from .data import data_import, data_export




# print('http://127.0.0.1:8000/knowledge-repo')
print('http://127.0.0.1:8000')
print('http://127.0.0.1:8000/manage')
# print('http://127.0.0.1:8000/blog')
# print('http://127.0.0.1:8000/books')
# print('http://127.0.0.1:8000/visuals')



def home(request):
    """Renders the home page. """


    return render(request,'blog/index.html')


def post_list(request):
    """Displays the posts."""

    blog_posts = BlogPost.objects.all()
    books = Book.objects.exclude(blog_display=False)

    posts_and_books = list(blog_posts) + list(books)
    posts_and_books.sort(reverse=True, key=lambda model: model.created)

    # Below loop creates a new list containing tuples for each post with the second tuple index containing the post type
    # such as 'Post' or 'Book'
    all_posts = []
    for i in range(len(posts_and_books)):
        all_posts.append((posts_and_books[i], posts_and_books[i].__class__.__name__))

    paginator = Paginator(all_posts, 7) 
    page = request.GET.get('page') # Look at paginator template to see how this value would be set.
   
    try:
        all_posts = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer then deliver the first page.
        all_posts = paginator.page(1)
    except EmptyPage:
        # If the page is out of range deliver the last page of results.
        all_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'all_posts': all_posts})


def post_detail(request, year, month, day, post):
    """Single Post"""

    # Below method raises an exception if the post is not found based on the url inputs provided.
    post = get_object_or_404(BlogPost, slug=post,                                  
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
            new_comment = True
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html',
                 {'post': post,
                 'comments': comments,
                 'new_comment': new_comment,
                 'comment_form': comment_form})




def book_list(request):
    """Renders the generic book list view"""

    books = Book.objects.order_by('-created')  
    return render(request, 'blog/book/list.html', {'books': books})
    

def book_detail(request, year, month, day, post):
    """Single Book"""

    # Below method raises an exception if the post is not found based on the url inputs provided.
    book_post = get_object_or_404(Book, slug=post,                                  
                                   created__year=year, 
                                   created__month=month,
                                   created__day=day)

    # List of active comments for this post
    comments = book_post.comments.filter(active=True) 
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create comment object but don't commit it to the database yet so you can link it to the post
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = book_post
            # Save the comment to the database
            new_comment.save()
            new_comment = True
    else:
        comment_form = CommentForm()

    return render(request, 'blog/book/detail.html',
                 {'book_post': book_post,
                 'comments': comments,
                 'new_comment': new_comment,
                 'comment_form': comment_form})

    



def knowledge_repo(request):
    """Produces the beautiful table of learning"""


    try:
        search_term = request.GET['search_box']
    except:
        search_term = ''

    if search_term == '':
        knowledge_list = Knowledge.objects.all()
    else:
        knowledge_list = Knowledge.objects.filter(Q(author__icontains=search_term) | Q(description__icontains=search_term)| Q(tags__icontains=search_term))


    return render(request, 'blog/knowledge_repo.html', {'knowledge_list': knowledge_list})



def question(request):
    """Render the question page"""
    questions = Question.objects.all()
    return render(request,'blog/questions.html', context={'questions': questions})



# def data_play(request):
#     """lolol"""
    
#     if request.method == 'POST':
#         #Depending on what button you click you will performa a different action

#         # First three are exporting of different data
#         if request.POST.get('Book'):            
#             data_export.export_db(Book)
#         elif request.POST.get('sql_import'):            
#             data_import.import_sql()
#         elif request.POST.get('Blog'):
#             data_export.export_db(Post)
#         elif request.POST.get('Knowledge'):
#             data_export.export_db(Knowledge)
#         elif request.POST.get('knowledge_import'):
#             data_import.import_knowledge()
#         elif request.POST.get('book_import'):
#             data_import.import_books()
#         elif request.POST.get('knowledge_update'):
#             data_import.update_knowledge()
#         elif request.POST.get('update_book'):
#             data_import.update_books()
#         elif request.POST.get('blog_update'):
#             data_import.import_blog()
            

#     return render(request, 'blog/data_import.html')

# def post_share(request, post_id):
#     """Sharing a post via email. This view handles both the processing of get request and post.
#     Currently there is no link on blog detail page to get to this. Need to fiddle with email stuff more first."""

#     post = get_object_or_404(Post, id=post_id)
#     sent = False

#     if request.method =='POST':
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             form_data = form.cleaned_data
#             post_url = request.build_absolute_uri(
#                 post.get_absolute_url())
#             subject = f"Yo. {form_data['name']} thinks you should read this post: {post.title}"
#             message = f"Read that shit at {post_url} \n\n My comments: {form_data['comments']}" # I have not tested after adding this line yet
#             send_mail(subject, message, 'brandtgreen97@gmail.com', [form_data['to']])
#             sent = True
#     else:
#         form = EmailPostForm()

#     return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})

