from django.shortcuts import render
from .models import Product


def products_view(request):
    products = Product.objects.all()
    return render(request, "productslist.html", {"products": products})
