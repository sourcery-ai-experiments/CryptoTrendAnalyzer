# Generated by Django 5.0.3 on 2024-04-06 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("market_trends", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExecutionLog",
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
                    "status",
                    models.IntegerField(help_text="Status da execução (200 para sucesso, 500 para erro)"),
                ),
                ("log", models.TextField(help_text="Log detalhado da execução")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Data e hora da criação do registro",
                    ),
                ),
            ],
        ),
    ]
