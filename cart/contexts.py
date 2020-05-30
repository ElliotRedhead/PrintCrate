from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """Enables access to cart items from all apps in project.

    Code modified from core CodeInstitute course content.
    Each product instance price is multiplied by quantity to calculate total
    price of the items in the cart.
    If product in cart has been removed from database the item is removed from
    cart.
    """
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0
    product_count = 0
    for item, quantity in list(cart.items()):
        try:
            product = Product.objects.get(pk=item)
            total += quantity * product.price
            product_count += quantity
            cart_items.append(
                {"id": item, "quantity": quantity, "product": product})
        except Product.DoesNotExist:
            cart.pop(item)
            request.session["cart"] = cart
    return {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count
    }
