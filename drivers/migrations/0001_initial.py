# Generated by Django 4.2.7 on 2023-11-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Driver",
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
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
