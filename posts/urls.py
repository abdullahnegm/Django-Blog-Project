from django.urls import path

from .views import *

app_name = "posts"

urlpatterns = [
    path('home', home, name="home"),
    path('<slug:slug>', detail, name="detail"),
    path('like/<slug>/<is_liked>', like, name="like"),
    path('subscribe/', like, name="like"),
    path('search/', search, name="search"),
    path('create/', create, name="create"),
    path('edit/<slug>', edit, name="edit"),
]