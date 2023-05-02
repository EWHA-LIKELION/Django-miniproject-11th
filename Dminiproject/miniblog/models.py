from django.db import models

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

    def __str__(self):
        return self.title
    
    