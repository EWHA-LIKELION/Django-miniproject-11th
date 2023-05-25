from django import forms
from .models import Main,Comment
from dataclasses import field

class Mainform(forms.ModelForm):
    class Meta:
        model=Main
        fields=['title','username','content','photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['username','comment_text']