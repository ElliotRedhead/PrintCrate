import random
from django.shortcuts import render
from products.models import Product


def home(request):
    """Renders the homepage with random selection from showcase products."""
    showcase_products = Product.objects.filter(
        showcase_product=True)
    products = []
    total_showcase_products = showcase_products.count()
    if total_showcase_products > 3:
        random_indices = random.Random().sample(
            range(0, total_showcase_products), 3
        )
        for index in random_indices:
            products.append(showcase_products.all()[index])
    elif total_showcase_products == 3:
        products = showcase_products
    return render(request, "home.html", {
        "page_title": "Home | PrintCrate",
        "products": products
    })
