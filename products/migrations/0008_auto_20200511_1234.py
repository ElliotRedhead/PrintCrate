# Generated by Django 3.0.5 on 2020-05-11 11:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_product_showcase_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(max_length=150),
        ),
    ]
