# Generated by Django 5.0.3 on 2024-03-31 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CurrencyData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pair",
                    models.CharField(
                        help_text="Pair of currencies (e.g., BRLBTC, BRLETH)",
                        max_length=12,
                    ),
                ),
                ("mms_20", models.FloatField(help_text="20-day simple moving average")),
                ("mms_50", models.FloatField(help_text="50-day simple moving average")),
                (
                    "mms_200",
                    models.FloatField(help_text="200-day simple moving average"),
                ),
                ("timestamp", models.DateTimeField()),
            ],
        ),
    ]