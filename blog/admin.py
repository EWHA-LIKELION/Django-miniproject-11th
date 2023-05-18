from django.contrib import admin
from .models import Blog, Comment, HashTag



admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(HashTag)

# Register your models here.
