from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """The registration form fields based on Django User model."""
    email = forms.EmailField()
    email.label = "Email"

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserCredentialsUpdateForm(forms.ModelForm):
    """Form providing fiels to update user credentials."""
    email = forms.EmailField(
        label="New Email Address",
        widget=forms.EmailInput(attrs={"placeholder": "Enter Email"}))

    password = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"}),
        validators=[validate_password])

    class Meta:
        model = User
        fields = ["email", "password"]
