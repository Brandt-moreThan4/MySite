from django.db import models




class PublishedManager(models.Manager):
    """custom manager. I think it returns a query that is automatically filtered for Post that are created... which is all of them"""
    # This is probably pointless right?
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='created')

class Post(models.Model):
    """Class to model a blog post. """
    
    #Maybe come back to add how to distinguish between blog and book and program post?
    #Also need to figure out how to make the date fields editable in admin interface
    
    #STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=250, unique_for_date='created') # I think this helps to make url strings
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    #status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')



    objects = models.Manager()
    published = CreatedManager() # This is probably pointless right?

    class Meta:
        """Sort posts by created date"""
        ordering = ('-created',)


    def __str__(self):
        """This is what shows up in admin page"""
        return self.title

