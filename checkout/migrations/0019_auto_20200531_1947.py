# Generated by Django 3.0.5 on 2020-05-31 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0010_auto_20200531_1252"),
        ("checkout", "0018_auto_20200531_1252"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderdetail",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="products.Product"
            ),
        ),
    ]
