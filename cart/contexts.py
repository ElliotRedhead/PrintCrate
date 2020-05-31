from products.models import Product
import sweetify


def database_stock_check(cart_quantity, product_availability):
    assert cart_quantity <= product_availability


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
    cart_adjusted = False
    for item, quantity in list(cart.items()):
        try:
            product = Product.objects.get(pk=item)
            try:
                database_stock_check(quantity, product.stock_available)
            except AssertionError:
                cart_adjusted = True
                quantity = product.stock_available
                if quantity == 0:
                    cart.pop(item)
                request.session["cart"] = cart
            finally:
                total += quantity * product.price
                product_count += quantity
                cart_items.append(
                    {"id": item, "quantity": quantity, "product": product})
        except Product.DoesNotExist:
            cart_adjusted = True
            cart.pop(item)
            request.session["cart"] = cart
    if cart_adjusted:
        print("The user's cart has been changed due to quantity restrictions.")
    return {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count
    }
