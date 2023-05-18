from django import forms
from .models import *

class Postform (forms.ModelForm):
    class Meta: 
        model=Posting
        fields =['title','body','category','image']

class Commentform (forms.ModelForm):
    class Meta: 
        model=Comment
        fields =['username','comment_text']