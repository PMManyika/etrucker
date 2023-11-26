from django.contrib import admin
from drivers.forms import DriverForm

from drivers.models import Driver


# Register your models here.
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "date_of_birth")
    form = DriverForm
