from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
import sweetify

# The contents of this file are closely based on the course content taught in
# the CodeInstitute Full Stack Web Development course.
# The teachings have been modified for the project owner's development style
# and to best suit the PrintCrate project.


def cart_view(request):
    if request.session["cart"] == {}:
        sweetify.error(
            request,
            "Your cart is empty.",
            text="Add products to your cart.",
            timer=4000,
            timerProgressBar=True,
            button=True
        )
        origin_page = request.META.get('HTTP_REFERER', '/')
        if origin_page.endswith("/cart/"):
            return redirect(reverse("products"))
        return HttpResponseRedirect(origin_page)
    else:
        return render(request, "cart.html")


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
