from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Shortener
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={"class": "form-control"}
    ))
    email = forms.CharField(label="Email", widget=forms.EmailInput(
        attrs={"class": "form-control"}
    ))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
       

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={"class": "form-control"}
    ))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))
    
    class Meta:
        model = Shortener
        fields = ('long_url',)