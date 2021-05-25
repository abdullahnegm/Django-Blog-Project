from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        "admin": "admin dashboard",
    }
    return render(request, 'auth/dashboard/home.html', context)
