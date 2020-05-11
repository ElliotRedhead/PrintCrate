from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerShippingForm


@login_required
def checkout_shipping_address_view(request):
    if request.method == "POST":
        customer_shipping = CustomerShippingForm(request.POST)
        if customer_shipping.is_valid():
            shipping = customer_shipping.save(commit=False)
            shipping.customer = request.user
            shipping.save()
            return redirect("home")
    else:
        form = CustomerShippingForm()

    return render(request, "checkout_shipping_address.html", {"page_title": "Shipping | PrintCrate", "customer_shipping_form": form})
