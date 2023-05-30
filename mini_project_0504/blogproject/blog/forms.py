from django import forms
from .models import Blog, Comment,HashTag

class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body', 'photo']


class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']