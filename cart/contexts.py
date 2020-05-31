import sweetify
from products.models import Product


def database_stock_check(cart_quantity, product_availability):
    """Test to determine if cart quantity exceeds quantity available."""
    assert cart_quantity <= product_availability


def database_product_active_check(product):
    """Test to determine if product is active on the store."""
    assert product.active_product


def cart_contents(request):
    """Enables access to cart items from all apps in project.

    Code modified from core CodeInstitute course content.
    Each product instance price is multiplied by quantity to calculate total
    price of the items in the cart.
    Database validation is conducted on each product, if the product fails
    validation it is removed from the user cart with a user feedback prompt.
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
                else:
                    cart[item] = quantity
                request.session["cart"] = cart
            finally:
                try:
                    database_product_active_check(product)
                except AssertionError:
                    cart_adjusted = True
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
        sweetify.error(
            request,
            title="One or more items have become unavailable",
            text="Please review your updated cart contents.",
            position="top-start",
            timer=4000,
            timerProgressBar=True,
            button=True
        )
    return {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count
    }
