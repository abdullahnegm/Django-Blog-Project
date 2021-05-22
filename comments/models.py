from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,related_name='replies')
    date = models.DateField(auto_now_add = True)
    content = models.TextField(max_length=150)
    