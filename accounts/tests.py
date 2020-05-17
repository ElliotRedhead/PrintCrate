from django.test import TestCase, Client
from django.contrib.auth import views as auth
from django.contrib.auth.models import User
from .forms import UserRegisterForm


class RegistrationFormTest(TestCase):
    def test_field_labels(self):
        """Tests if field labels exist and are correct."""
        form = UserRegisterForm()
        self.assertTrue(form.fields["username"].label == "Username")
        self.assertTrue(form.fields["email"].label == "Email")
        self.assertTrue(form.fields["password1"].label == "Password")
        self.assertTrue(
            form.fields["password2"].label == "Password confirmation")

    def test_field_help_prompts(self):
        """Tests if Django help text tips are displayed for applicable fields, email field not included as validated via other means."""
        form = UserRegisterForm()
        self.assertTrue(form.fields["username"].help_text ==
                        "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
        self.assertTrue(form.fields["password1"].help_text ==
                        "<ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>")
        self.assertTrue(form.fields["password2"].help_text ==
                        "Enter the same password as before, for verification.")

    def test_successful_submission(self):
        """Tests if form is determined to be valid given valid input."""
        form_data = {
            "username": "testuser",
            "email": "testemail@domain.com",
            "password1": "thisisasecret101",
            "password2": "thisisasecret101"
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())


class LoginViewTest(TestCase, Client):
    def client_setup(self):
        self.client = Client()

    def test_login_page_responds_with_url_call(self):
        """Tests if a view is loaded upon calling the login URL.

        The test responds positively with 200,
        test fails if status code 404 expected."""
        response = self.client.get(
            "/accounts/login", {"template_name": "login.html"})
        self.assertEqual(response.status_code, 200)

    def test_successful_submission(self):
        User.objects.create_user(
            username="testuser", password="thisisasecret101")
        response = self.client.post(
            "/accounts/login", {"template_name": "login.html", "username": "testuser", "password": "thisisasecret101"}, follow=True)
        self.assertTrue(response.context["user"].is_active)
