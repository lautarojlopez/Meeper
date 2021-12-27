from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import fields

from Usuarios.models import Perfil

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

class FormEditarUsuario(forms.ModelForm):
    first_name = forms.CharField()
    first_name.widget.attrs['class'] = 'p-2 focus:outline-none border border-gray-300 rounded-lg'
    class Meta:
        model = User
        fields = ['first_name']

class FormEditarPerfil(forms.ModelForm):
    img = forms.ImageField()
    img.widget.attrs['class'] = 'p-2 focus:outline-none border border-gray-300 rounded-lg'
    bio = forms.CharField(required=False)
    bio.widget.attrs['class'] = 'p-3 focus:outline-none border resize-none border-gray-300 rounded-lg'
    bio.widget.attrs['rows'] = 3
    bio.widget.attrs['cols'] = 10
    class Meta:
        model = Perfil
        fields = ['bio', 'img']