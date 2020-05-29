from django.shortcuts import render
from products.models import Product
import random


def home(request):
    showcase_products = Product.objects.filter(
        showcase_product=True)
    total_showcase_products = showcase_products.count()
    random_indices = random.Random().sample(range(0, total_showcase_products), 3)
    products = []
    for index in random_indices:
        products.append(showcase_products.all()[index])
    return render(request, "home.html", {"page_title": "Home | PrintCrate", "products": products})
