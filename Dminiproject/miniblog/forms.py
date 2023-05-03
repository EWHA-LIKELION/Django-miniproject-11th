from django import forms
from .models import Main

class Mainform(forms.ModelForm):
    class Meta:
        model=Main
        fields=['title','username','content']