from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.db.models import Q

from .models import Category, Post
from comments.models import *
# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('-publish')
    categories = Category.objects.all()
    context = {
        "posts": posts,
        "categories": categories
    }
    return render(request, 'posts/home.html', context)

def detail(request, slug):
    post = get_object_or_404(Post,slug=slug)
    comments = post.comments.filter(parent__isnull=True)
    is_liked = post.likes.filter(username=request.user.username).exists()
    is_disliked = post.dislikes.filter(username=request.user.username).exists()

    context = {
        "post": post,
        "comments": comments,
        "is_liked": is_liked,
        "is_disliked": is_disliked
    }
    return render(request, 'posts/detail.html', context)

def search(request):
    field = request.GET['search']
    posts = Post.objects.filter(Q(title__icontains=field) | Q(content__icontains=field)) # change it to tags later
    categories = Category.objects.all()

    context = {
        "posts": posts,
        "categories": categories
    }
    return render(request, 'posts/home.html', context)
    

def like(request, slug, is_liked):
    post = get_object_or_404(Post, slug=slug)
    if is_liked == "True":
        post.likes.remove(request.user)
        post.dislikes.add(request.user)
    else:
        post.likes.add(request.user)
        post.dislikes.remove(request.user)
    if post.dislikes.count() >= 10:
        post.delete()
        return redirect('posts:home')
    return redirect(reverse('posts:detail', kwargs={"slug": slug}))

    

def subscribe(request, id):
    pass