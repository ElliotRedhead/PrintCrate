from django.urls import path

urlpatterns = [
    path("", cart_view, name="cart_view")
]
