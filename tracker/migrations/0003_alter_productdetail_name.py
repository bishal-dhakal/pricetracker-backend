# Generated by Django 5.0 on 2023-12-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0002_remove_pricehistory_product_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productdetail",
            name="name",
            field=models.CharField(default=None, max_length=200),
        ),
    ]
