from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import CustomerShippingForm, PaymentForm
import sweetify
import stripe
from products.models import Product
from .models import CustomerShipping, OrderDetail
from cart.contexts import cart_contents
from cart.views import empty_cart_modal

stripe.api_key = settings.STRIPE_SECRET


@login_required
def checkout_shipping_address_view(request):
    if not request.session.get("cart"):
        empty_cart_modal(request)
        return redirect("products")
    if request.method == "POST":
        customer_shipping = CustomerShippingForm(request.POST)
        if customer_shipping.is_valid():
            shipping = customer_shipping.save(commit=False)
            shipping.customer = request.user
            shipping.save()
            return redirect("payment")
    else:
        form = CustomerShippingForm()
    return render(request, "checkout_shipping_address.html", {"page_title": "Shipping | PrintCrate", "customer_shipping_form": form})


@login_required
def checkout_payment(request):
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            cart = request.session.get("cart", {})
            cart_total = cart_contents(request)["total"]
            try:
                customer = stripe.Charge.create(
                    amount=int(cart_total*100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data["stripe_id"]
                )
            except stripe.error.CardError:
                sweetify.error(
                    request,
                    "Payment error occurred, please retry with valid credentials."
                )
            else:
                sweetify.success(
                    request,
                    "Payment successful, thank you for your purchase."
                )
                for item, quantity in cart.items():
                    product = get_object_or_404(
                        Product, pk=item)
                    product_total = quantity * product.price
                    order_detail = OrderDetail(
                        shipping=CustomerShipping.objects.filter(
                            customer=request.user).last(),
                        product=product,
                        quantity=quantity,
                        total=product_total,
                    )
                    order_detail.save()
                del request.session["cart"]
                return redirect(reverse("profile"))
    else:
        payment_form = PaymentForm()
    return render(request, "checkout_payment.html", {
        "page_title": "Payment | PrintCrate",
        "payment_form": payment_form,
        "publishable": settings.STRIPE_PUBLISHABLE
    })
