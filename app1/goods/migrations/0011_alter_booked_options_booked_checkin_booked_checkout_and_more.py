# Generated by Django 4.2.13 on 2024-05-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0010_booked"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="booked",
            options={
                "ordering": ("id",),
                "verbose_name": "Бронювання",
                "verbose_name_plural": "Бронювання",
            },
        ),
        migrations.AddField(
            model_name="booked",
            name="checkin",
            field=models.DateField(default="2024-01-01", verbose_name="Дата заїзду"),
        ),
        migrations.AddField(
            model_name="booked",
            name="checkout",
            field=models.DateField(default="2024-01-01", verbose_name="Дата виїзду"),
        ),
        migrations.AddField(
            model_name="booked",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="Електронна пошта"
            ),
        ),
        migrations.AddField(
            model_name="booked",
            name="phone",
            field=models.CharField(blank=True, max_length=20, verbose_name="Телефон"),
        ),
        migrations.AlterField(
            model_name="booked",
            name="name",
            field=models.CharField(max_length=150, unique=True, verbose_name="І'мя"),
        ),
        migrations.AlterModelTable(
            name="booked",
            table="booked",
        ),
    ]
