from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify, title


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 30)



# class Subscribe(models.Model):
#     user = models.ManyToManyField(User, related_name="user")
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField(max_length = 600)
    image = models.ImageField(upload_to = "posts")
    publish = models.DateField(auto_now_add = True)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(primary_key=True, db_index=True)
    likes = models.ManyToManyField(User, related_name="likes")
    dislikes = models.ManyToManyField(User, related_name="dislikes")
    # tags

    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(**kwargs)


    def __str__(self):
        return self.title
