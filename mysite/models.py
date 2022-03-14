from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.contrib import auth




class Post(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=2000)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                              null=True)
    date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post_page', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


class Comments(models.Model):
    comment = models.TextField





