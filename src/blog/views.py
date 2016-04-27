from django.shortcuts import render
from .forms import BlogSpot

# Create your views here.
def home(request):
    form = BlogSpot()
    title = "Eat My Snow"
    context = {
        "title": title,
        "form": form
    }
    return render(request,"blog_home.html",context)


