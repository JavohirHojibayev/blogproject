from django.db import models
from django.contrib.auth.models import User



class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        app_label = 'blog'

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models
    class Meta:
        app_label = 'blog'
