from typing import Any
from django.db import models

# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment