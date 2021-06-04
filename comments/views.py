from comments.forms import commentForm
from django.shortcuts import get_object_or_404, redirect, render
from posts.models import Badwords

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

        # replacing bad words with stars
        for w in Badwords.objects.values_list('badword',flat=True):
            wordLength = len(w)
            stars=''
            for x in range(0,wordLength):
                stars=stars+"*"
            content = content.replace(w,stars)

        parent = get_object_or_404(Comment, id=request.POST["reply"]) if "reply" in request.POST else None

        comment = Comment(user=request.user, post=post, content=content, parent=parent)
        
        
        comment.save()
    
    return redirect(reverse("posts:detail", kwargs={"slug": slug}))