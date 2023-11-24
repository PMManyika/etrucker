# Generated by Django 4.2.7 on 2023-11-24 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("drivers", "0001_initial"),
        ("expenses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="driver",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="drivers.driver",
            ),
        ),
        migrations.DeleteModel(
            name="Driver",
        ),
    ]