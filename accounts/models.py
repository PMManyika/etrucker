from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=100,
        choices=[
            ("driver", "Driver"),
            ("dispatcher", "Dispatcher"),
            ("customer", "Customer"),
        ],
    )


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
