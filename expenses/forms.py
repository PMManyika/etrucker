# forms.py

from django import forms
from .models import Expense, ServiceRecord
from vehicles.models import Vehicle


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["vehicle", "amount", "expense_type", "description"]


class ServiceRecordForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        fields = ["vehicle", "service_date", "service_details", "cost"]


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["make", "model", "year", "registration_number", "driver"]
