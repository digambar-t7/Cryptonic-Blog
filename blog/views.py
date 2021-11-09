from django.shortcuts import render,HttpResponse
from .models import BlogPost

# Create your views here.
def bloghome(request):
    posts = BlogPost.objects.all()
    blogs = {
        'posts':posts,
    }
    return render(request,'blog/home.html',blogs)

def blogpost(request,slug):
    print(slug)
    post = BlogPost.objects.filter(slug=slug).first()
    print(post)
    return render(request,'blog/blogpost.html',{'post':post})