import stripe
import sweetify
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from cart.contexts import cart_contents
from cart.views import empty_cart_modal
from products.models import Product

from .forms import CustomerShippingForm, PaymentForm
from .models import CustomerShipping, OrderDetail

stripe.api_key = settings.STRIPE_SECRET


@login_required
def checkout_shipping_address_view(request):
    """Constructs the shipping address information form.

    Accessing user must be logged in with items in cart.
    Shipping info is linked to the user but allows the user to
    specify a new shipping address with each transaction if wanted.
    """
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
    return render(
        request,
        "checkout_shipping_address.html",
        {"page_title": "Shipping | PrintCrate", "customer_shipping_form": form},
    )


@login_required
def checkout_payment(request):
    """Conducts a test Stripe charge.

    If payment is successful the order creation is triggered and
    the user's cart is cleared.
    """
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            cart = request.session.get("cart", {})
            cart_total = cart_contents(request)["total"]
            try:
                stripe.Charge.create(
                    amount=int(cart_total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data["stripe_id"],
                )
            except stripe.error.CardError:
                sweetify.error(
                    request,
                    title="Payment error occurred, please check your credentials.",
                    text="If error persists, contact site owner.",
                    icon="error",
                )
            except stripe.error.InvalidRequestError:
                sweetify.error(
                    request,
                    title="A payment error has occurred.",
                    text="An item may have gone out of stock during checkout.",
                    icon="error",
                )
                return redirect("profile")
            except stripe.error.APIConnectionError:
                sweetify.error(
                    request,
                    title="A payment error has occurred.",
                    text="Connection to payment handler failed, please retry later.",
                    icon="error",
                )
                return redirect("profile")
            else:
                sweetify.success(
                    request,
                    title="Payment successful, thank you for your purchase.",
                    icon="success",
                )
                create_order_product_records(request, cart)
                del request.session["cart"]
                return redirect(reverse("profile"))
    else:
        payment_form = PaymentForm()
    return render(
        request,
        "checkout_payment.html",
        {
            "page_title": "Payment | PrintCrate",
            "payment_form": payment_form,
            "publishable": settings.STRIPE_PUBLISHABLE,
        },
    )


def create_order_product_records(request, cart):
    """Creates the product order record in the database.

    The product's available stock is decreased by the purchased quantity.
    """
    for item, quantity in cart.items():
        product = get_object_or_404(Product, pk=item)
        product_total = quantity * product.price
        product.stock_available -= quantity
        product.save()
        order_detail = OrderDetail(
            shipping=CustomerShipping.objects.filter(customer=request.user).last(),
            product=product,
            quantity=quantity,
            total=product_total,
        )
        order_detail.save()
