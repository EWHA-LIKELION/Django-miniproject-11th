from django.db import models


#모델건들면 migration


class Posting(models.Model):
    title=models.CharField('Title',max_length=200)
    date=models.DateTimeField('date published') 
    body=models.TextField('Content')
    image = models.ImageField(upload_to = "images/", null=True, blank=True)
    category = models.CharField('week',max_length=10,null=True,default='')

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]
    