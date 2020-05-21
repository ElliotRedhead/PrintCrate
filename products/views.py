from django.shortcuts import render
from django.db.models import Q
from .models import Product


def products_view(request):
    products = Product.objects.all()
    return render(request, "productslist.html", {"products": products, "page_title": "Products | PrintCrate"})


def product_detail_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "productdetail.html", {"product": product})


def product_search(request):
    search_query = ["baby", "phone"]
    q_object = Q(name__icontains=search_query[0]) | Q(
        description__icontains=search_query[0])
    for term in search_query:
        q_object.add((Q(name__icontains=term) | Q(
            description__icontains=term)), q_object.connector)
    products = Product.objects.filter(q_object)
    return render(request, "productslist.html", {"products": products, "page_title": "Products | PrintCrate"})
