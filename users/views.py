from django.shortcuts import redirect, render
from .forms import *
# Create your views here.


def register(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/home')


    context = {
        "form": form
    }
    return render(request, 'auth/register.html', context)