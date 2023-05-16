from django import forms
from .models import Blog,Comment
from dataclasses import field

class Blogform(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['type','title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username','comment_text']