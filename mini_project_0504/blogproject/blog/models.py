#from typing import Any, Set
from django.db import models
from django.utils import timezone
#from django.urls import reverse

# Create your models here.

class HashTag(models.Model):
    hashtag=models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag

class Blog(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField('date published')
    body=models.TextField()
    hashtag=models.ManyToManyField(HashTag)
    photo=models.ImageField(blank=True, null=True, upload_to="blog_photo")


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.comment
    
