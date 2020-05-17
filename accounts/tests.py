from django.test import TestCase
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm


class RegistrationFormTest(TestCase):
    def test_field_labels(self):
        """Tests if field labels exist and are correct."""
        form = UserRegisterForm(UserCreationForm)
        self.assertTrue(form.fields["username"].label == "Username")
        self.assertTrue(form.fields["email"].label == "Email")
        self.assertTrue(form.fields["password1"].label == "Password")
        self.assertTrue(
            form.fields["password2"].label == "Password confirmation")
