# Generated by Django 5.0.1 on 2024-05-07 03:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='no_of_likes',
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(null=True, related_name='postlikes', to=settings.AUTH_USER_MODEL),
        ),
    ]