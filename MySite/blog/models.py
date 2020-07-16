from django.db import models
from django.urls import reverse




class Post(models.Model):
    """Class to model a blog post. """
    
    #Maybe come back to add how to distinguish between blog and book and program post?
    #Also need to figure out how to make the date fields editable in admin interface
    
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=250, unique_for_date='created') # I think this helps to make url strings
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

        
    class Meta:
        """Sort posts by created date"""
        ordering = ('-created',)


    def __str__(self):
        """This is what shows up in admin page"""
        return self.title


    def get_absolute_url(self):
        """Retrieve the absolute url for a post"""
        # I do not understand how this works.
        return reverse('blog:post_detail',
                       args=[self.created.year,
                             self.created.month,
                             self.created.day,
                             self.slug])
