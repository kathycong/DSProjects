from django.db import models
#import url resolvers
from django.core.urlresolvers import reverse

# Create your models here.

#class for each blog posts
#this class has access to all the code that's in this class and it becomes a part of this class
class Post(models.Model):
    #below are properties of each posts
    title = models.CharField(max_length = 255) #inputs
    slug = models.SlugField(max_length = 255, unique=True) #inputs
    summary = models.CharField(max_length=300) #inputs
    content = models.TextField() #text field
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img")

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s'% self.title
        
    def get_absolute_url(self):
        return reverse('blog.views.post', args = [self.slug])
        




