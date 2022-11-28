# Generated by Django 4.1.3 on 2022-11-26 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("type", models.CharField(max_length=50)),
                ("date", models.DateField()),
                ("value", models.FloatField()),
                ("cpf", models.IntegerField()),
                ("card", models.CharField(max_length=12)),
                ("hour", models.DateTimeField()),
                ("owner", models.CharField(max_length=14)),
                ("shop", models.CharField(max_length=19)),
                ("sign", models.CharField(max_length=1)),
            ],
        ),
    ]