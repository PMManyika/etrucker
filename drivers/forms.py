from django import forms
from .models import Driver


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["user", "phone", "date_of_birth", "license_image"]
