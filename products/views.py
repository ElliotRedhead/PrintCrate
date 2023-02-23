from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from .models import Product


def paginator_setup(request, products):
    """Creates paginator, tracks current page and how many objects per page."""
    paginator = Paginator(products, 15)
    page_object = paginator.get_page(request.GET.get("page"))
    return page_object


def products_view(request):
    """Displays all store-active products with pagination."""
    products = Product.objects.filter(active_product=True)
    paginator_info = paginator_setup(request, products)
    return render(
        request,
        "productslist.html",
        {
            "products": products,
            "page_title": "Products | PrintCrate",
            "page_object": paginator_info,
        },
    )


def product_detail_view(request, primary_key):
    """Displays detailed product view."""
    previous_page = request.headers.get("referer")
    if previous_page is None:
        previous_page = "/products"
    product = Product.objects.get(pk=primary_key)
    return render(
        request,
        "productdetail.html",
        {
            "product": product,
            "page_title": f"{product.name} | PrintCrate",
            "previous_page": previous_page,
        },
    )


def product_search(request):
    """Searches for products containing search terms in name or description."""
    search_query = request.GET.get("search_query")
    search_query_list = search_query.split(" ")
    q_object = Q(name__icontains=search_query_list[0]) | Q(
        description__icontains=search_query_list[0]
    )
    for term in search_query_list:
        q_object.add(
            (Q(name__icontains=term) | Q(description__icontains=term)),
            q_object.connector,
        )
    products = Product.objects.filter(q_object, active_product=True)
    paginator_info = paginator_setup(request, products)
    return render(
        request,
        "productslist.html",
        {
            "products": products,
            "page_title": "Products | PrintCrate",
            "search_query": search_query,
            "page_object": paginator_info,
        },
    )
