from django.urls import path

from .views import *

app_name = "comments"

urlpatterns = [
    path("comment/create/<slug>", create, name="create")
]