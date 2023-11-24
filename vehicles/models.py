from django.db import models
from drivers.models import *


class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    registration_number = models.CharField(max_length=50)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
