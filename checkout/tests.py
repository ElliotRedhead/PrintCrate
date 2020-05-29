from django.test import TestCase, Client
from django.contrib.auth.models import User
from products.models import Product
from .models import CustomerShipping


class TestCheckoutInfoView(TestCase):
    """Tests for the checkout info/shipping page."""

    def client_setup(self):
        """Creates new client to conduct isolated unit tests."""
        self.client = Client()

    def test_redirect_if_user_not_logged_in(self):
        """Tests if non-authenticated user is redirected to login page."""
        response = self.client.get("/checkout/shipping/")
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/checkout/shipping/", follow=True)
        self.assertRedirects(
            response, "/accounts/login?next=/checkout/shipping/")

    def test_redirect_if_user_logged_empty_cart(self):
        """Tests if an authenticated user is redirected with empty cart."""
        User.objects.create_user(
            username="testuser", password="thisisasecret101")
        self.client.login(username="testuser", password="thisisasecret101")
        response = self.client.get("/checkout/shipping/")
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/checkout/shipping/", follow=True)
        self.assertRedirects(response, "/products/")

    def test_page_loads_if_user_logged_with_cart_items(self):
        """Tests if authenticated user loads page with cart contents."""
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
        response = self.client.get("/checkout/shipping/")
        self.assertEqual(response.status_code, 200)

    def test_submission_of_shipping_information_creates_object(self):
        """Tests if object is correctly created upon user submission."""
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
        self.client.post("/checkout/shipping/", {
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

    def test_checkout_custom_templates_rendered_with_successful_call(self):
        """Tests if correct templates are rendered upon calling checkout URL.

        Placeholder data is used to successfully access the checkout page.
        """
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
        response = self.client.get("/checkout/shipping/")
        self.assertTemplateUsed(response, "checkout_shipping_address.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "layout/head.html")
        self.assertTemplateUsed(response, "components/navbar.html")
        self.assertTemplateUsed(response, "components/footer.html")
        self.assertTemplateUsed(response, "layout/scripts.html")

    def test_checkout_third_party_templates_rendered_with_successful_call(self):
        """Tests if third-party templates are rendered upon calling checkout URL.

        Placeholder data is used to successfully access the checkout page.
        """
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
        response = self.client.get("/checkout/shipping/")
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
