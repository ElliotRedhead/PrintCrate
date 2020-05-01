from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

# The contents of this file are closely based on the course content taught in
# the CodeInstitute Full Stack Web Development course.
# The teachings have been modified for the project owner's development style
# and to best suit the PrintCrate project.


def cart_view(request):
    if request.session["cart"] == {}:
        messages.error(request, "Your cart is empty")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
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
