from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    nickname=models.CharField(max_length=100)
    university=models.CharField(max_length=50)
    location=models.CharField(max_length=200)
    age=models.IntegerField(default=0)
    gender=models.CharField(default='여성', max_length=50)
    travelcities=models.CharField(default='서울', max_length=100)
