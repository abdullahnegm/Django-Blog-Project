from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.db.models import Q

from .models import Category, Post
from comments.models import *
from .forms import *
from comments.forms import *
from FinalBlog.settings import MEDIA_ROOT
import os
from dashboard.forms import PostsForm

# from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    categories = Category.objects.all()
    
    post = Post.objects.get(slug="laravellaravel")
    for cat in post.categories.all():
        print(cat)
    if 'category' in request.GET and categories.filter(name = request.GET['category']):
        posts = Post.objects.filter(categories__name = request.GET['category'])
    else:
        posts = Post.objects.all().order_by('-publish')

    context = {
        "posts": posts,
        "categories": categories
    }
    return render(request, 'posts/home.html', context)


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(parent__isnull=True)
    is_liked = post.likes.filter(username=request.user.username).exists()
    is_disliked = post.dislikes.filter(username=request.user.username).exists()

    comment_form = commentForm()

    context = {
        "post": post,
        "comments": comments,
        "is_liked": is_liked,
        "is_disliked": is_disliked,
        "comment_form": comment_form
    }
    return render(request, 'posts/detail.html', context)


def search(request):
    field = request.GET['search']
    posts = Post.objects.filter(Q(title__icontains=field) | Q(
        content__icontains=field))  # change it to tags later
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

# @login_required
def create(request):
    form = PostsForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        post = Post(title=form.cleaned_data['title'], content=form.cleaned_data['content'] , image=form.cleaned_data['image'])
        post.user = request.user
        post.save()

        for id in form.cleaned_data['categories']:
            category = get_object_or_404(Category, id=int(id))
            post.categories.add(category)

        if request.user.is_staff:
            return redirect('dashboard:home')

        return redirect('posts:home')

    context = {
        "form": form
    }
    return render(request, "posts/create.html", context)

def edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.user:
        return redirect(reverse('posts:detail', kwargs={'slug': slug}))
    form = postForm(request.POST or None, request.FILES or None, initial={
        "title": post.title,
        "content": post.content,
        "image": post.image,
        "categories": [ category.id for category in post.categories.all() ]
        })
    if request.method == 'POST' and form.is_valid():
        if post.image != form.cleaned_data["image"]:
            os.remove(os.path.join(MEDIA_ROOT, f"{post.image}"))

        post.title=form.cleaned_data['title']
        post.content=form.cleaned_data['content']
        post.image=form.cleaned_data['image']
        post.user = request.user
        post.save()

        for id in form.cleaned_data['categories']:
            category = get_object_or_404(Category, id=int(id))
            post.categories.add(category)

        return redirect(reverse('posts:detail', kwargs={"slug":slug}))

    context = {
        "form": form,
        "slug": slug
    }
    return render(request, 'posts/edit.html', context)

def delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.user:
        return redirect(reverse('posts:detail', kwargs={'slug':slug}))
    post.delete()
    return redirect('posts:home')