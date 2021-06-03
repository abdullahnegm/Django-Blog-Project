from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from dashboard.forms import BadwordsForm, CategoriesForm, UserForm
from posts.models import Badwords
from posts.models import Category
from django.contrib.auth.models import User
from dashboard.forms import BadwordsForm, CategoriesForm, PostsForm
from comments.forms import commentForm
from posts.models import *
import os
from django.urls import reverse
from FinalBlog.settings import MEDIA_ROOT
# Create your views here.

# home


def home(request):
    context = {
        "admin": "admin dashboard",
    }
    return render(request, 'auth/dashboard/home.html', context)

# badwords


def all_badwords(request):
    badwords = Badwords.objects.all()
    context = {"data": badwords}
    return render(request, 'auth/dashboard/badwords/badwords.html', context)


def badwords_details(request, badword_id):
    badword = Badwords.objects.get(id=badword_id)
    context = {"data": badword}
    return render(request, 'auth/dashboard/badwords/badwords_details.html', context)


def add_badwords(request):
    badwords_form = BadwordsForm()
    if request.method == 'POST':
        badwords_form = BadwordsForm(request.POST)
        if badwords_form.is_valid():
            badwords_form.save()
            return HttpResponseRedirect("/auth/badwords")

    context = {"badwords_form": badwords_form, 'editable': False}
    return render(request, 'auth/dashboard/badwords/badwords_form.html', context)


def edit_badwords(request, badword_id):
    badwords = Badwords.objects.get(id=badword_id)
    badwords_form = BadwordsForm(instance=badwords)
    if request.method == 'POST':
        badwords_form = BadwordsForm(request.POST, instance=badwords)
        if badwords_form.is_valid():
            badwords_form.save()
            return HttpResponseRedirect('/auth/badwords')

    context = {'badwords_form': badwords_form, 'editable': True}
    return render(request, 'auth/dashboard/badwords/badwords_form.html', context)


def delete_badwords(request, badword_id):
    badwords = Badwords.objects.get(id=badword_id)
    badwords.delete()
    return HttpResponseRedirect("/auth/badwords")


# categories

def all_categories(request):
    categories = Category.objects.all()
    context = {"data": categories}
    return render(request, 'auth/dashboard/categories/categories.html', context)


def add_categories(request):
    categories_form = CategoriesForm()
    if request.method == 'POST':
        categories_form = CategoriesForm(request.POST)
        if categories_form.is_valid():
            categories_form.save()
            return HttpResponseRedirect("/auth/categories")

    context = {"categories_form": categories_form, 'editable': False}
    return render(request, 'auth/dashboard/categories/categories_form.html', context)


def categories_details(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {"data": category}
    return render(request, 'auth/dashboard/categories/categories_details.html', context)


def edit_categories(request, category_id):
    categories = Category.objects.get(id=category_id)
    categories_form = CategoriesForm(instance=categories)
    if request.method == 'POST':
        categories_form = CategoriesForm(request.POST, instance=categories)
        if categories_form.is_valid():
            categories_form.save()
            return HttpResponseRedirect('/auth/categories')

    context = {'categories_form': categories_form, 'editable': True}
    return render(request, 'auth/dashboard/categories/categories_form.html', context)


def delete_categories(request, category_id):
    categories = Category.objects.get(id=category_id)
    categories.delete()
    return HttpResponseRedirect("/auth/categories")

# users


def all_users(request):
    users = User.objects.all()
    context = {"data": users}
    return render(request, 'auth/dashboard/users/users.html', context)


def add_user(request):
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect("/auth/users")

    context = {"user_form": user_form}
    return render(request, 'auth/dashboard/users/users_form.html', context)


def user_details(request, user_id):
    user = User.objects.get(id=user_id)
    context = {"data": user}
    return render(request, 'auth/dashboard/users/users_details.html', context)


def block(request, user_id):
    user = User.objects.get(id=user_id)
    if user.is_active:
        user.is_active = False
    user.save()
    return HttpResponseRedirect("/auth/users")


def un_block(request, user_id):
    user = User.objects.get(id=user_id)
    if not user.is_active:
        user.is_active = True
    user.save()
    return HttpResponseRedirect("/auth/users")


def promote(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()
    return HttpResponseRedirect("/auth/users")


def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return HttpResponseRedirect("/auth/users")

# posts


def all_posts(request):
    posts = Post.objects.all()
    context = {"data": posts}
    return render(request, 'auth/dashboard/posts/posts.html', context)


def add_posts(request):
    form = PostsForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        post = Post(
            title=form.cleaned_data['title'], content=form.cleaned_data['content'], image=form.cleaned_data['image'])
        post.user = request.user
        post.save()
        for id in form.cleaned_data['categories']:
            category = get_object_or_404(Category, id=int(id))
            post.categories.add(category)
        return redirect('dashboard:allposts')
    context = {
        "post_form": form
    }
    return render(request, "auth/dashboard/posts/posts_form.html", context)


def edit_posts(request, slug):
    post = get_object_or_404(Post, slug=slug)

    form = PostsForm(request.POST or None, request.FILES or None, initial={
        "title": post.title,
        "content": post.content,
        "image": post.image,
        "categories": [category.id for category in post.categories.all()]
    })
    if request.method == 'POST' and form.is_valid():
        if post.image != form.cleaned_data["image"]:
            os.remove(os.path.join(MEDIA_ROOT, f"{post.image}"))

        post.title = form.cleaned_data['title']
        post.content = form.cleaned_data['content']
        post.image = form.cleaned_data['image']
        post.user = request.user
        post.save()

        for id in form.cleaned_data['categories']:
            category = get_object_or_404(Category, id=int(id))
            post.categories.add(category)

        return redirect(reverse('dashboard:postdetails', kwargs={"slug": slug}))

    context = {
        "form": form,
        "post": post
    }
    return render(request, 'auth/dashboard/posts/posts_edit.html', context)


def posts_details(request, slug):
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
    return render(request, 'auth/dashboard/posts/posts_details.html', context)


def delete_posts(request, slug):
    posts = Post.objects.get(slug=slug)
    posts.delete()
    return HttpResponseRedirect("/auth/posts")
