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

    def test_field_help_prompts(self):
        """Tests if Django help text tips are displayed for applicable fields, email field not included as validated via other means."""
        form = UserRegisterForm(UserCreationForm)
        self.assertTrue(form.fields["username"].help_text ==
                        "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
        self.assertTrue(form.fields["password1"].help_text ==
                        "<ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>")
        self.assertTrue(form.fields["password2"].help_text ==
                        "Enter the same password as before, for verification.")
