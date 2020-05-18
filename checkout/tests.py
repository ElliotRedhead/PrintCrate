from django.test import TestCase, Client
from django.contrib.auth.models import User
from products.models import Product
from .models import CustomerShipping


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

    def test_page_loads_if_user_logged_with_cart_items(self):
        User.objects.create_user(
            username="testuser", password="thisisasecret101")
        self.client.login(username="testuser", password="thisisasecret101")
        item = Product(name="Product",
                       product_image="testing_img.jpg",
                       description="Product description.",
                       price="20.00",
                       stock_available="5",
                       showcase_product="True")
        item.save()
        session = self.client.session
        session["cart"] = {1: 1}
        session.save()
        response = self.client.get("/checkout/info/")
        self.assertEqual(response.status_code, 200)

    def test_submission_of_shipping_information_creates_object(self):
        User.objects.create_user(
            username="testuser", password="thisisasecret101")
        self.client.login(username="testuser", password="thisisasecret101")
        item = Product(name="Product",
                       product_image="testing_img.jpg",
                       description="Product description.",
                       price="20.00",
                       stock_available="5",
                       showcase_product="True")
        item.save()
        session = self.client.session
        session["cart"] = {1: 1}
        session.save()
        self.client.post("/checkout/info/", {
            "full_name": "Homer Simpson",
            "primary_address_line": "742",
            "secondary_address_line": "Evergreen Terrace",
            "town_or_city": "Springfield",
            "county": "Undetermined",
            "postcode": "SI54 7JU",
            "country": "United States",
            "phone_number": "76484377"
        })
        shipping = CustomerShipping.objects.first()
        self.assertEqual(shipping.full_name, "Homer Simpson")
        self.assertEqual(shipping.primary_address_line, "742")
        self.assertEqual(shipping.secondary_address_line, "Evergreen Terrace")
        self.assertEqual(shipping.town_or_city, "Springfield")
        self.assertEqual(shipping.county, "Undetermined")
        self.assertEqual(shipping.postcode, "SI54 7JU")
        self.assertEqual(shipping.country, "United States")
        self.assertEqual(shipping.phone_number, "76484377")
