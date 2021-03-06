# Generated by Django 3.2.3 on 2021-05-22 10:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=600)),
                ('image', models.ImageField(upload_to='posts')),
                ('publish', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('categories', models.ManyToManyField(to='posts.Category')),
                ('dislikes', models.ManyToManyField(related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
