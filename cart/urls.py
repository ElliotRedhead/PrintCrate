from django.urls import path, re_path

from .views import add_to_cart, adjust_cart, cart_view

urlpatterns = [
    path("", cart_view, name="cart_view"),
    re_path(r"add/(?P<id>\d+)", add_to_cart, name="add_to_cart"),
    re_path(r"adjust/(?P<id>\d+)", adjust_cart, name="adjust_cart"),
]
