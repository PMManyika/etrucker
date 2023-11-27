# admin.py

from django.contrib import admin
from .models import Expense, Vehicle, Driver, ServiceRecord
from .forms import ExpenseForm, VehicleForm, ServiceRecordForm


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("date", "amount", "expense_type", "description")
    form = ExpenseForm


@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "service_date", "service_details", "cost")
    form = ServiceRecordForm
