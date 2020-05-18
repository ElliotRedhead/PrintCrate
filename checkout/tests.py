from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestCheckoutInfoView(TestCase):
    def client_setup(self):
        """Creates new client to conduct isolated unit tests."""
        self.client = Client()

    def test_redirect_if_user_not_logged_in(self):
        """Tests if non-authenticated user is redirected to login page."""
        response = self.client.get("/checkout/info/")
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/checkout/info/", follow=True)
        self.assertRedirects(response, "/accounts/login?next=/checkout/info/")

    def test_redirect_if_user_logged_empty_cart(self):
        User.objects.create_user(
            username="testuser", password="thisisasecret101")
        self.client.login(username="testuser", password="thisisasecret101")
        response = self.client.get("/checkout/info/")
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/checkout/info/", follow=True)
        self.assertRedirects(response, "/products/")
