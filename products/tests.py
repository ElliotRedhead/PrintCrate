from django.test import TestCase
from .models import Product


class ProductTest(TestCase):
    "Tests if product returns correct name."

    def test_product_name_returned(self):
        "Correct product name is returned."
        product = Product(name="Test Design")
        self.assertEqual("Test Design", product.name)
