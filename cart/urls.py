from django.urls import path, include
from .views import cart_view

urlpatterns = [
    path("", view_cart, name="view_cart"),
    re_path(r"add/(?P<id>\d+)", add_to_cart, name="add_to_cart"),
    re_path(r"adjust/(?P<id>\d+)", adjust_cart, name="adjust_cart"),
]
