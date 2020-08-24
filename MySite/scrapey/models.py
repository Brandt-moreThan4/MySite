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


    def get_template_name(self) -> str:
        """Return the name of the appropriate html template to render for the detail view."""

        if self.name == 'Aswath Damodaron Blog':
            return 'aswath.html'
        elif self.name == 'Eugene Wei Blog':
            return 'eugene.html'
        elif self.name == 'Stratechery':
            return 'stratechery.html'
        elif self.name == 'Collaborative Fund':
            return 'collab.html'
        elif self.name == 'OSAM':
            return 'OSAM.html'
        elif self.name == 'Amnesia':
            return 'amnesia.html'
        elif self.name == 'Gates Notes':
            return 'gates.html'

    def get_logo(self) -> str:
        """Return the string logo path for the post""" 
        if self.name == 'Aswath Damodaron Blog':
            return '../../static/scrapey/images/blog_logos/Aswath.jpg'
        elif self.name == 'Eugene Wei Blog':
            return '../../static/scrapey/images/blog_logos/stratechery.png'
        elif self.name == 'Stratechery':
            return '../../static/scrapey/images/blog_logos/stratechery.png'
        elif self.name == 'Collaborative Fund':
            return '../../static/scrapey/images/blog_logos/collaborative.png'
        elif self.name == 'OSAM':
            return '../../static/scrapey/images/blog_logos/OSAM.png'
        elif self.name == 'Amnesia':
            return '../../static/scrapey/images/blog_logos/amnesia.jpg'
        elif self.name == 'Gates Notes':
            return '../../static/scrapey/images/blog_logos/gates.jpg'

        

    class Meta:
        ordering = ('-date',)




