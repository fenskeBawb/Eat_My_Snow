from django.db import models


# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    caption = models.CharField(max_length=1000, blank=True, null=True)
    # media =
    timestamp = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title
