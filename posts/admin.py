from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    exclude = ['slug']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)