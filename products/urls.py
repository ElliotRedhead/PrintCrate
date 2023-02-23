from django.urls import path

from .views import product_detail_view, product_search, products_view

urlpatterns = [
    path("", products_view, name="products"),
    path("detail/<int:primary_key>", product_detail_view, name="product_detail"),
    path("search", product_search, name="product_search"),
]
