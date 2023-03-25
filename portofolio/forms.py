from django import forms
from django.forms import ModelForm

from .models import post

class PostForm(ModelForm):

    class Meta:
        model = post
        fields = '__all__'
    
        widgets = {
            'tags' :forms.CheckboxSelectMultiple(),
        }