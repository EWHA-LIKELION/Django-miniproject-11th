from django.contrib import admin
from .models import Main,Comment,HashTag

# Register your models here.
admin.site.register(Main)
admin.site.register(Comment)
admin.site.register(HashTag)