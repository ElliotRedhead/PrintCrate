from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """The registration form fields based on Django User model."""
    email = forms.EmailField()
    email.label = "Email"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
