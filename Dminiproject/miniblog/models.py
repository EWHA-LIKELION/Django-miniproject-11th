from django.db import models
from django.utils import timezone

class HashTag(models.Model):
    hashtag=models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag

# Create your models here.
class Main(models.Model):
    title=models.CharField(max_length=30)
    uploaddate=models.DateTimeField('date published')
    #opendate=models.DateTimeField('date published')
    #updatedate=models.DateTimeField(auto_now=True)
    username=models.CharField(max_length=10)
    content=models.TextField()
    #image=models.ImageField(upload_to="miniblog/image",null=True,blank=True)
    #null=True 데이터베이스 상에서 null 값 허용
    #blank=True 입력을 받을 때 입력이 없어도 된다는 뜻 (이거 없으면 사진 업로드 안하면 게시물 업로드 못해!)
    hashtag=models.ManyToManyField(HashTag)
    photo=models.ImageField(blank=True, null=True, upload_to="main_photo")

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post=models.ForeignKey(Main, related_name='comments',on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text


