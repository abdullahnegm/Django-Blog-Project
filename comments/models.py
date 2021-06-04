from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    date = models.DateField(auto_now_add = True)
    content = models.TextField(max_length=150)
    
    def is_parent(self):
        return self.parent is None

    is_parent.boolean = True
    is_parent.short_description = "Parent"

    def __str__(self):
        return self.user.username