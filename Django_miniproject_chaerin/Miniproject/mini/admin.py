from django.contrib import admin
from .models import *
#from .models import Category
# Register your models here.

admin.site.register(Posting)
admin.site.register(Comment)
admin.site.register(HashTag)
