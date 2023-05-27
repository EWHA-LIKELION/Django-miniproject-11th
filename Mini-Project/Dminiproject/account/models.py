from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    nickname=models.CharField(max_length=10) #닉네임
    favorite=models.CharField(max_length=50) #최애배우
    interest=models.CharField(max_length=30) #최애극