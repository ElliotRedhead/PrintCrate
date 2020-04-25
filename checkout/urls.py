from django.urls import path
from .views import checkout_shipping_address_view

urlpatterns = [
    path("info/", checkout_shipping_address_view, name="shipping")
]
