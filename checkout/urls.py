from django.urls import path
from .views import checkout_shipping_address_view, checkout_payment

urlpatterns = [
    path("shipping/", checkout_shipping_address_view, name="shipping"),
    path("payment/", checkout_payment, name="payment"),
]
