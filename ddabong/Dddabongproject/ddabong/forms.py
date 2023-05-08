from django import forms
from .models import Ddabong

class Ddabongform(forms.ModelForm):
    class Meta :
        model = Ddabong
        fields = ['title', 'body']