from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=25)
    product_image = models.ImageField(
        upload_to="product_images",
        blank=True
    )
    description = models.CharField(max_length=150)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.00)])
    stock_available = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0)])
    showcase_product = models.BooleanField(default=False)
    active_product = models.BooleanField(default=True)

    def __str__(self):
        return self.name
