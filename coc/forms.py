from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class UserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' ,'placeholder': "Enter your username"})) 
    player_tag  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' ,'placeholder': "Enter your player tag"}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' ,'placeholder': "Enter your phone no with ISD code"})) 
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control' ,'placeholder': "Enter your emailid"}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control' ,'placeholder': "Enter your password"}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control' ,'placeholder': "Enter your password again"}))

    class Meta:
        model = User
        fields = ('username', 'player_tag', 'phone_no', 'email', 'password1', 'password2', )