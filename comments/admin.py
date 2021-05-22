from django.contrib import admin
from django.db.models.fields import BooleanField
from .models import *
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "is_parent"]



admin.site.register(Comment, CommentAdmin)