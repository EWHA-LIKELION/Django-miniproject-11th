from django.db import models
from django.utils import timezone

# Create your models here.

class HashTag(models.Model):
    hashtag = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag

class Blog(models.Model):
    type = models.CharField(max_length=200,default='') #공연명
    title = models.CharField(max_length=200,default='') #게시물 제목
    date = models.DateTimeField('date published') #게시 날짜
    body = models.TextField('Content',default='') #본문
    hashtag=models.ManyToManyField(HashTag)

    def __str__(self):
        return self.type
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:45]
    
class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text