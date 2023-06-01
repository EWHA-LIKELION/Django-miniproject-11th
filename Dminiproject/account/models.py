from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractUser):
    nickname=models.CharField(max_length=100)
    #university=models.CharField(max_length=100)
    #location=models.CharField(max_length=100)
    birth=models.DateTimeField(default=timezone.now())
    age=models.IntegerField(default=20)
    motto=models.CharField(max_length=500, default="안녕")
    
