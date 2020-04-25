from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomerShippingForm


@login_required
def checkout_shipping_address_view(request):
    return render(request, "checkout_shipping_address.html", {"page_title": "Shipping | PrintCrate", "customer_shipping_form": CustomerShippingForm})
