from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
import sweetify

# The contents of this file are closely based on the course content taught in
# the CodeInstitute Full Stack Web Development course.
# The teachings have been modified for the project owner's development style
# and to best suit the PrintCrate project.


def cart_view(request):
    """Handles request for displaying the contents of the cart.

    User is returned to their original page if attempting to access an empty cart, with a modal message to alert that the cart is empty with prompt to add products.
    If user has emptied their cart they are navigated to the products page, with the modal triggered.
    """
    origin_page = request.META.get('HTTP_REFERER', '/')
    empty_cart_modal = sweetify.error(
        request,
        "Your cart is empty.",
        text="Add products to your cart.",
        timer=4000,
        timerProgressBar=True,
        button=True
    )
    if "cart" in request.session:
        if request.session["cart"] == {}:
            empty_cart_modal
            if origin_page.endswith("/cart/"):
                return redirect(reverse("products"))
            return HttpResponseRedirect(origin_page)
        else:
            return render(request, "cart.html")
    else:
        empty_cart_modal
        return redirect(origin_page)


def add_to_cart(request, id):
    quantity = int(request.POST.get("quantity"))

    cart = request.session.get("cart", {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session["cart"] = cart
    return redirect(reverse("cart_view"))


def adjust_cart(request, id):
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session["cart"] = cart
    return redirect(reverse("cart_view"))
