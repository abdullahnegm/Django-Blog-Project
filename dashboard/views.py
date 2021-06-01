from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from dashboard.forms import BadwordsForm, CategoriesForm
from posts.models import Badwords
from posts.models import Category
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    context = {
        "admin": "admin dashboard",
    }
    return render(request, 'auth/dashboard/home.html', context)


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

    context = {"badwords_form": badwords_form}
    return render(request, 'auth/dashboard/badwords/badwords_form.html', context)


def edit_badwords(request, badword_id):
    badwords = Badwords.objects.get(id=badword_id)
    badwords_form = BadwordsForm(instance=badwords)
    if request.method == 'POST':
        badwords_form = BadwordsForm(request.POST, instance=badwords)
        if badwords_form.is_valid():
            badwords_form.save()
            return HttpResponseRedirect('/auth/badwords')

    context = {'badwords_form': badwords_form}
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

    context = {"categories_form": categories_form}
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

    context = {'categories_form': categories_form}
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
    context = {"data": "users"}
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
