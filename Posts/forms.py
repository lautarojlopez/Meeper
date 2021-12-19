from django import forms
from django.forms import fields
from .models import Post

class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']