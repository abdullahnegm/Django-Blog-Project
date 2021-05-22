from django.shortcuts import render

from .models import Post
from comments.models import *
# Create your views here.


def home(request):
    posts = Post.objects.all()
    # comments = Comment.objects.filter()
    context = {
        "posts": posts
    }
    return render(request, 'posts/home.html', context)