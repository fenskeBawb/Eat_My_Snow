from django.db import models


# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    caption = models.TextField(max_length=1000, blank=True, null=True)
    media = models.FileField()
    timestamp = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return 'view_blog_category', None, { 'slug': self.slug }