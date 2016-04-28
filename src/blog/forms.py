from django import forms

from .models import blog

class BlogSpot(forms.ModelForm):
    class Meta:
        model = blog[9]
        fields = ['title', 'caption', 'media']

    # class clean_blog(self):
    #     pass #cleans old blog posts from database if more storage is needed

