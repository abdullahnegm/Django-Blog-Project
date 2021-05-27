from django.urls import path
from django.urls.conf import include
from dashboard import views

app_name = "dashboard"

urlpatterns = [
    path('auth/home', views.home),
    # Badwords urls
    path("auth/badwords", views.all_badwords),
    path("auth/add/badword", views.add_badwords),
    path("auth/badword_details/<badword_id>", views.badwords_details),
    path("auth/badword/edit/<badword_id>", views.edit_badwords),
    path("auth/badword/delete/<badword_id>", views.delete_badwords)
]
