# Generated by Django 3.0.5 on 2020-05-31 11:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0009_auto_20200526_0943"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="active_product",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="stock_available",
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
