from django.db import models
from django.utils import timezone


#모델건들면 migration

class HashTag(models.Model):
    hashtag=models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag

class Posting(models.Model):
    # TYPE_CHOICES = (
    #     ('월요일', '월요일'),
    #     ('화요일', '화요일'),
    #     ('수요일', '수요일'),
    #     ('목요일', '목요일'),
    #     ('금요일', '금요일'),
    #     ('토요일', '토요일'),
    #     ('일요일', '일요일')
    # )
    title=models.CharField('Title',max_length=200)
    date=models.DateTimeField('date published') 
    body=models.TextField('Content')
    image = models.ImageField(upload_to = "images/", null=True, blank=True)
    # category = models.CharField('week',max_length=10,choices=TYPE_CHOICES)
    category = models.CharField('week',max_length=10,null=True,default='')
    hashtag=models.ManyToManyField(HashTag)

    def __str__(self):
        return "{}-{}".format(self.category,self.title)
    
    def summary(self):
        return self.body[:20]
    
class Comment(models.Model):
    post=models.ForeignKey(Posting, related_name='comments',on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.comment_text
    

