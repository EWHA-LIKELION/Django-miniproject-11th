from dataclasses import field
from django import forms
from .models import Ddabong, Comment

class Ddabongform(forms.ModelForm):
    class Meta :
        model = Ddabong
        fields = ['title', 'body', 'photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'comment_text']