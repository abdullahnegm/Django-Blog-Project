from django.shortcuts import render

# Create your views here.

from comments.forms import commentForm
from django.shortcuts import get_object_or_404, redirect, render

from django.urls import reverse
from .models import *
# Create your views here.


def create(request, slug):
    form = commentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():

        content = form.cleaned_data["content"]
        post = get_object_or_404(Post, slug=slug)

        # if "reply" in request.POST:
        #     parent = get_object_or_404(Comment, id=request.POST["reply"])
        parent = get_object_or_404(Comment, id=request.POST["reply"]) if "reply" in request.POST else None

        comment = Comment(user=request.user, post=post, content=content, parent=parent)
        comment.save()
    
    return redirect(reverse("dashboard:postdetails", kwargs={"slug": slug}))