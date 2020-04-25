from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def checkout_shipping_address_view(request):
    return render(request, "checkout_shipping_address.html", {"page_title": "Shipping | PrintCrate"})
