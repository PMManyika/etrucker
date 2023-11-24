# admin.py

from django.contrib import admin
from expenses.models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ["make", "model", "year", "registration_number", "driver"]
    search_fields = ["make", "model", "registration_number"]
