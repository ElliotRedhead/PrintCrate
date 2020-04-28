from django.shortcuts import render
from .models import Product


def products_view(request):
    products = Product.objects.all()
    return render(request, "productslist.html", {"products": products, "page_title": "Products | PrintCrate"})


def product_detail_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "productdetail.html", {"product": product})
