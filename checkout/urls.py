from django.urls import path

from .views import checkout_payment, checkout_shipping_address_view

urlpatterns = [
    path("shipping/", checkout_shipping_address_view, name="shipping"),
    path("payment/", checkout_payment, name="payment"),
]
