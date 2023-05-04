from django.db import models

# Create your models here.

class Blog(models.Model):
    type=models.CharField(max_length=200,default='') #공연명
    title=models.CharField(max_length=200,default='') #게시물 제목
    date=models.DateTimeField('date published') #게시 날짜
    body=models.TextField('Content',default='') #본문

    def __str__(self):
        return self.type
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:45]
