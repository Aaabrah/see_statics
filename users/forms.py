from django import forms

from .models import UserModel
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': "username",
        'class': 'form-control',
        'placeholder': 'username'

    }), label=False)

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'password'
    }), label=False)


class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'username',
        'type': 'username',
        'name': 'username',
        'class': 'form-control',
        'placeholder': 'username'
    }), label=False)

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'id': "email",
        'type': "email",
        'name': "email",
        'class': 'form-control',
        'placeholder': 'email'
    }), label=False)

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password',
        'type': 'password',
        'class': 'form-control pwstrength',
        'data-indicator': 'pwindicator',
        'name': 'password',
        'placeholder': 'password',
    }), label=False)

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password2',
        'type': 'password',
        'name': 'password-confirm',
        'class': 'form-control',
        'placeholder': 'confirm password'
    }), label=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        user = UserModel.objects.get(username=username)
        if user:
            raise ValidationError(f'Ushbu {username} isimli username band')
        return self.cleaned_data['username']

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Parol birhil emas')
        return self.cleaned_data['confirm_password']
