from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager



class PostBase(models.Model):
    """Generic post class that Book, Blog, and Program post can inherit from"""
    post_title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique_for_date='created') # I think this helps to make url strings
    post_body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateField(auto_now=True)
    display = models.BooleanField(default=True)

    class Meta:
        # abstract = True
        ordering = ('-created',)


class BlogPost(PostBase):
    """Class to model a blog post. """
    
    # I do not need any specific fields for blog post. And meta ordering is taken care of in PostBase as well


    def __str__(self):
        """This is what shows up in admin page"""
        return self.post_title


    def get_absolute_url(self):
        """Retrieve the absolute url for a post"""
        # I do not understand how this works.
        return reverse('blog:post_detail',
                       args=[self.created.year,
                             self.created.month,
                             self.created.day,
                             self.slug])


class Book(PostBase):
    """Class to model book data"""
    book_title = models.CharField(max_length=300)    
    author = models.CharField(max_length=300)
    blog_display = models.BooleanField(default=False)
    cover_image = models.ImageField(default='Nothing_Yet', upload_to='book_images/')


    def __str__(self):
        """This is what shows up in admin page"""
        return self.book_title


    def get_author(self):
        """Author text is stored like "Last; First" But causes an error if a comma is used instead for storage"""
        try:
            named_reversed = self.author.split(';')
            name_normal = named_reversed[1].strip() + ' ' + named_reversed[0].strip()
        except:
            name_normal = 'Author Error'
        
        return name_normal


    def get_absolute_url(self):
        """Retrieve the absolute url for a book detail"""

        return reverse('blog:book_detail',
                       args=[self.created.year,
                             self.created.month,
                             self.created.day,
                             self.slug])


class Comment(models.Model):
    """Comments on posts"""
    post = models.ForeignKey(PostBase, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True) # This field will allow admins to hide inappropriate comments

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


class Knowledge(models.Model):
    """Class to model a knowledge record"""

    author = models.CharField(max_length=500)
    description = models.TextField()
    source = models.TextField()
    tags = models.TextField(default='Placeholder')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def tags_as_list(self):
        try:
            return self.tags.split(';')
        except:
            return ['Error']


class Question(models.Model):
    """Represents a question for my questions page"""
    
    question = models.TextField()
    category = models.TextField(default='Uncategorized') 



