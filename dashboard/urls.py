from django.urls import path

from .views import *

app_name = "dashboard"

urlpatterns = [
    path('auth/home', home, name="home"),
]
