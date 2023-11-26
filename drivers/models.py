from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    license_image = models.ImageField(
        upload_to="drivers_licenses/", null=True, blank=True
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    class Meta:
        verbose_name = _("Driver")
        verbose_name_plural = _("Drivers")
