# Generated by Django 4.2.7 on 2023-11-24 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0002_alter_vehicle_driver_delete_driver"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicle",
            name="driver",
        ),
    ]