# Generated by Django 4.2.13 on 2024-05-23 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0014_products_rooms"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="products",
            name="checkin",
        ),
        migrations.RemoveField(
            model_name="products",
            name="checkout",
        ),
    ]
