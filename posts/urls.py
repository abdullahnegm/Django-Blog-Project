from django.urls import path

from .views import *

app_name = "posts"

urlpatterns = [
    path('home', home, name="home"),
    path('<slug:slug>', detail, name="detail"),
    path('create/', create, name="create"),
    path('delete/<slug>', delete, name="delete"),
]