from django.db import models
from django.contrib.auth.models import User
from drivers.models import *
from vehicles.models import Vehicle


class Expense(models.Model):
    EXPENSE_TYPES = [
        ("FUEL", "Fuel"),
        ("SERVICE", "Service"),
        ("TOLL", "Toll"),
        ("OTHER", "Other"),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPES)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.expense_type} - ${self.amount}"


class ServiceRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service_date = models.DateField()
    service_details = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Service on {self.service_date}"
