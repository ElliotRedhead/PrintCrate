from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00)])
    stock_available = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)])

    def __str__(self):
        return self.name
