from django.shortcuts import render
from products.models import Product


def home(request):
    products = Product.objects.filter(showcase_product=True)
    return render(request, "home.html", {"page_title": "Home | PrintCrate", "products": products})
