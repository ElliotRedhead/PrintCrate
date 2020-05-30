from django.test import TestCase, Client
from django.contrib.auth import views as auth
from django.contrib.auth.models import User
from .forms import UserRegisterForm


class RegistrationFormTest(TestCase):
    """Test registration form validation."""

    def test_field_labels(self):
        """Test if field labels exist and are correct."""
        form = UserRegisterForm()
        self.assertTrue(form.fields["username"].label == "Username")
        self.assertTrue(form.fields["email"].label == "Email")
        self.assertTrue(form.fields["password1"].label == "Password")
        self.assertTrue(
            form.fields["password2"].label == "Password confirmation")

    def test_field_help_prompts(self):
        """Test if Django help text tips are displayed for applicable fields.

        The email field is not included as validated via other means.
        """
        form = UserRegisterForm()
        self.assertTrue(form.fields["username"].help_text == "Required. "
                        "150 characters or fewer. "
                        "Letters, digits and @/./+/-/_ only.")
        self.assertTrue(form.fields["password1"].help_text ==
                        "<ul><li>Your password can’t be too similar "
                        "to your other personal information.</li>"
                        "<li>Your password must contain at least "
                        "8 characters.</li><li>Your password can’t be a "
                        "commonly used password.</li><li>Your password "
                        "can’t be entirely numeric.</li></ul>")
        self.assertTrue(form.fields["password2"].help_text ==
                        "Enter the same password as before, for verification.")

    def test_successful_submission(self):
        """Test if form is determined to be valid given valid input."""
        form_data = {
            "username": "testuser",
            "email": "testemail@domain.com",
            "password1": "thisisasecret101",
            "password2": "thisisasecret101"
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())


class RegistrationViewTest(TestCase, Client):
    """Test the user registration view functionality."""

    def client_setup(self):
        """Create new client to conduct isolated unit tests."""
        self.client = Client()

    def test_registration_page_responds_with_url_call(self):
        """Test if a view is loaded upon calling the login URL.

        The test passes with 200 (success),
        test fails if other status codes e.g. 404 (not found) are returned.
        """
        response = self.client.get(
            "/accounts/register", {"template_name": "register.html"})
        self.assertEqual(response.status_code, 200)

    def test_registration_correct_user_templates_rendered_with_call(self):
        """Test if correct templates are rendered upon calling register URL.

        Bootstrap and django-specific templates are omitted from this test.
        """
        response = self.client.get("/accounts/register")
        self.assertTemplateUsed(response, "register.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "components/footer.html")
        self.assertTemplateUsed(response, "components/navbar.html")
        self.assertTemplateUsed(response, "layout/head.html")
        self.assertTemplateUsed(response, "layout/scripts.html")

    def test_registration_third_party_templates_rendered_with_call(self):
        """Test third party templates used with register URL."""
        response = self.client.get("/accounts/register")
        self.assertTemplateUsed(response, "bootstrap4/uni_form.html")
        self.assertTemplateUsed(response, "bootstrap4/errors.html")
        self.assertTemplateUsed(response, "bootstrap4/field.html")
        self.assertTemplateUsed(response, "django/forms/widgets/text.html")
        self.assertTemplateUsed(response, "django/forms/widgets/input.html")
        self.assertTemplateUsed(response, "django/forms/widgets/attrs.html")
        self.assertTemplateUsed(
            response, "bootstrap4/layout/help_text_and_errors.html")
        self.assertTemplateUsed(
            response, "bootstrap4/layout/field_errors_block.html")
        self.assertTemplateUsed(response, "bootstrap4/layout/help_text.html")
        self.assertTemplateUsed(response, "django/forms/widgets/email.html")
        self.assertTemplateUsed(response, "django/forms/widgets/password.html")


class LoginViewTest(TestCase, Client):
    """Tess the user login view functionality."""

    def client_setup(self):
        """Create new client to conduct isolated unit tests."""
        self.client = Client()

    def test_login_page_responds_with_url_call(self):
        """Test if a view is loaded upon calling the login URL.

        The test passes with 200 (success),
        test fails if other status codes e.g. 404 (not found) are returned.
        """
        response = self.client.get(
            "/accounts/login", {"template_name": "login.html"})
        self.assertEqual(response.status_code, 200)

    def test_login_correct_user_templates_rendered_with_call(self):
        """Test if correct templates are rendered upon calling login URL.

        Bootstrap and django-specific templates are omitted from this test.
        """
        response = self.client.get("/accounts/login")
        self.assertTemplateUsed(response, "login.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "components/footer.html")
        self.assertTemplateUsed(response, "components/navbar.html")
        self.assertTemplateUsed(response, "layout/head.html")
        self.assertTemplateUsed(response, "layout/scripts.html")

    def test_login_correct_third_party_templates_rendered_with_call(self):
        """Test if third party templates are used upon calling login URL."""
        response = self.client.get("/accounts/login")
        self.assertTemplateUsed(response, "bootstrap4/uni_form.html")
        self.assertTemplateUsed(response, "bootstrap4/errors.html")
        self.assertTemplateUsed(response, "bootstrap4/field.html")
        self.assertTemplateUsed(response, "django/forms/widgets/text.html")
        self.assertTemplateUsed(response, "django/forms/widgets/input.html")
        self.assertTemplateUsed(response, "django/forms/widgets/attrs.html")
        self.assertTemplateUsed(
            response, "bootstrap4/layout/help_text_and_errors.html")
        self.assertTemplateUsed(
            response, "bootstrap4/layout/field_errors_block.html")
        self.assertTemplateUsed(response, "bootstrap4/layout/help_text.html")
        self.assertTemplateUsed(response, "django/forms/widgets/password.html")

    def test_successful_submission(self):
        """Test if user is logged in with valid credentials.

        An example user is created in the database, credentials
        for that user are then submitted in the login view.
        The user is then deemed active if login was successful.
        """
        User.objects.create_user(
            username="testuser", password="thisisasecret101")
        response = self.client.post(
            "/accounts/login",
            {"template_name": "login.html",
             "username": "testuser",
             "password": "thisisasecret101"},
            follow=True)
        self.assertTrue(response.context["user"].is_active)
