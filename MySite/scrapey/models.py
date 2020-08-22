from django.db import models
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    """Generic post class that Book, Blog, and Program post can inherit from"""
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique_for_date='date') # I think this helps to make url strings
    body = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=300)
    url = models.TextField()
    website = models.TextField()
    name = models.CharField(max_length=300)



    def __str__(self):
        """This is what shows up in admin page"""
        return self.title


    def get_absolute_url(self):
        """Retrieve the absolute url for a post"""
        # I do not understand how this works.
        return reverse('scrapey:post_detail',
                       args=[self.date.year,
                             self.date.month,
                             self.date.day,
                             self.slug])


    class Meta:
        ordering = ('-date',)




