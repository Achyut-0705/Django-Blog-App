from django.db import models
from Portal.settings import BASE_DIR
from django.contrib.auth.models import User
from django.utils import timezone
import os

class Client(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    title = models.CharField(blank=True, max_length=5)
    firstname = models.CharField(blank=True, max_length=30)
    lastname = models.CharField(blank=True, max_length=30)
    email = models.EmailField(blank=True, max_length=254)
    phone = models.CharField(blank=True, max_length=10)

class Post(models.Model):
    path = os.path.join(BASE_DIR, 'media')
    title = models.CharField(max_length=100)
    thumbnail = models.FileField(upload_to=path)
    thumnail_path = models.FilePathField(path = path)
    description = models.TextField()
    dateposted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete= models.CASCADE)