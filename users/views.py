from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import *
# Create your views here.


def register(request):
    form = UserForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('users:login')
    context = {
        "form": form
    }
    return render(request, 'auth/register.html', context)



def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/admin/')
            return redirect('posts:home')
    context = {
        "form": form
    }
    return render(request, 'auth/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('posts:home')


def promote(request, id):
    user = get_object_or_404(User, id=id)
    user.is_staff = True
    user.is_superuser = True
    user.save()

    return redirect(reverse("posts:detail", kwargs={"slug": request.POST['slug']}))


def block(request, id):
    user = get_object_or_404(User, id=id)
    user.is_active = False if user.is_active else True
    user.save()
    return redirect(reverse("posts:detail", kwargs={"slug": request.POST['slug']}))