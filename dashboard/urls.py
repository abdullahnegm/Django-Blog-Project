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
    path("auth/badword/delete/<badword_id>", views.delete_badwords),

    # categories urls
    path("auth/categories", views.all_categories),
    path("auth/add/category", views.add_categories),
    path("auth/category_details/<category_id>", views.categories_details),
    path("auth/category/edit/<category_id>", views.edit_categories),
    path("auth/category/delete/<category_id>", views.delete_categories),

    # users urls
    path("auth/users", views.all_users),
    path("auth/add/user", views.add_user),
    path("auth/user_details/<user_id>", views.user_details),
    path("auth/user/block/<user_id>", views.block),
    path("auth/user/unblock/<user_id>", views.un_block),
    path("auth/user/promote/<user_id>", views.promote),
    path("auth/user/delete/<user_id>", views.delete_user),


    # posts urls
    path("auth/posts", views.all_posts, name="allposts"),
    path("auth/add/post", views.add_posts, name="addnewpost"),
    path("auth/post_details/<slug>", views.posts_details, name="postdetails"),
    path("auth/post/edit/<slug>", views.edit_posts, name="editpost"),
    path("auth/post/delete/<slug>", views.delete_posts, name="deletepost")
]
