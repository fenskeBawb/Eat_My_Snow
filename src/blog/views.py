from django.shortcuts import render
from .forms import BlogSpot

# Create your views here.
def home(request):
    blog1 = BlogSpot()
    title = "Eat My Snow"
    context = {
        "title": title,
        "blog1": blog1
    }
    return render(request,"blog_home.html",context)


