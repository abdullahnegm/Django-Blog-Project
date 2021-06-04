from django.urls import path

from .views import *

from django.contrib.auth import views as auth_views

app_name = "users"


urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("promote/<id>/", promote, name="promote"),
    path("block/<id>/", block, name="block"),
]