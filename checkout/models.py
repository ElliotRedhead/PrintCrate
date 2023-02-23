import datetime

from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class CustomerShipping(models.Model):
    """Model detailing shipping information for an order."""

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=False)
    primary_address_line = models.CharField(max_length=50, blank=False)
    secondary_address_line = models.CharField(max_length=50, blank=True, null=True)
    town_or_city = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=50, blank=False)
    postcode = models.CharField(max_length=10, blank=False)
    country = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f"{self.id}-{self.customer}"


class OrderDetail(models.Model):
    """Model containing order details."""

    shipping = models.ForeignKey(CustomerShipping, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    purchase_date = models.DateField(default=datetime.date.today, blank=True)
    order_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity}-{self.product.name}-{self.purchase_date}-£{self.total}"
