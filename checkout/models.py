import datetime
from django.db import models
from django.contrib.auth.models import User


class CustomerShipping(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=False)
    primary_address_line = models.CharField(max_length=50, blank=False)
    secondary_address_line = models.CharField(
        max_length=50, blank=True, null=True)
    town_or_city = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=50, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    purchase_date = models.DateField(default=datetime.date.today, blank=True)

    def __str__(self):
        return f"{self.id}-{self.purchase_date}-{self.customer}"
