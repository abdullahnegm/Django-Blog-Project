# Generated by Django 3.2.3 on 2021-06-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_badwords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='categories', to='posts.Category'),
        ),
    ]
