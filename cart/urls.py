from django.urls import path, include, re_path
from .views import cart_view, add_to_cart, adjust_cart, remove_from_cart

urlpatterns = [
    path("", cart_view, name="cart_view"),
    re_path(r"add/(?P<id>\d+)", add_to_cart, name="add_to_cart"),
    re_path(r"adjust/(?P<id>\d+)", adjust_cart, name="adjust_cart"),
    re_path(r"remove/(?P<id>\d+)", remove_from_cart, name="remove_from_cart")
]
