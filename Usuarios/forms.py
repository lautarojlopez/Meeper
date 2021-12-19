from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import fields

class UserRegisterForm(UserCreationForm):
    
    def clean_first_name(self):
        if not self.cleaned_data['first_name']:
            raise ValidationError("Este campo es obligatorio.")
        return self.cleaned_data['first_name']

    def clean_email(self):
        if not self.cleaned_data['email']:
            raise ValidationError("Este campo es obligatorio.")
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']