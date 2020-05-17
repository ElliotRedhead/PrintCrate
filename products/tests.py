from django.test import TestCase, Client
from .models import Product
from .views import products_view


class ProductModelTest(TestCase):
    """Tests if product returns correct name."""

    def test_product_name_returned(self):
        """Correct product name is returned."""
        product = Product(name="Test Design")
        self.assertEqual("Test Design", product.name)


class ProductViewTest(TestCase, Client):
    """Tests if products list view is displayed."""

    def client_setup(self):
        self.client = Client()

    def test_products_list_page_responds_with_url_call(self):
        """Tests if a view is loaded upon calling the products URL.

        The test responds positively with 200, 
        test fails if status code 404 expected.
        """
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
