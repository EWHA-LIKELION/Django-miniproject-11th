from django import forms
from .models import Posting

class Blogform (forms.ModelForm):
    class Meta: 
        model=Posting
        fields =['title','body','category','image']