from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .data import data_import


# print('http://127.0.0.1:8000')
print('http://127.0.0.1:8000/blog-external/')
print('http://127.0.0.1:8000/blog-external/data/')



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


def data_play(request):
    """!!!"""
    
    if request.method == 'POST':
        #Depending on what button you click you will performa a different action

        button_value = request.POST.get('Button')
        
        if button_value == 'sql':            
            data_import.import_sql()        
            

    return render(request, 'scrapey/data.html')





# def post_detail(request, year, month, day, post):
#     """Single Post"""

#     # Below method raises an exception if the post is not found based on the url inputs provided.
#     post = get_object_or_404(BlogPost, slug=post,                                  
#                                    created__year=year, 
#                                    created__month=month,
#                                    created__day=day)

#     # List of active comments for this post
#     comments = post.comments.filter(active=True) 
#     new_comment = None

#     if request.method == 'POST':
#         # A comment was posted
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create comment object but don't commit it to the database yet so you can link it to the post
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#             new_comment = True
#     else:
#         comment_form = CommentForm()

#     return render(request, 'blog/post/detail.html',
#                  {'post': post,
#                  'comments': comments,
#                  'new_comment': new_comment,
#                  'comment_form': comment_form})