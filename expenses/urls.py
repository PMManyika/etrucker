# expenses/urls.py

from django.urls import path
from . import views
from drivers.views import *

urlpatterns = [
    path("", views.expense_list, name="expense_list"),
    path("new/", views.expense_create, name="expense_create"),
    path("<int:id>/edit/", views.expense_update, name="expense_update"),
    path("<int:id>/delete/", views.expense_delete, name="expense_delete"),
    path("drivers/", driver_list, name="driver_list"),
    path("drivers/new/", driver_create, name="driver_create"),
    path("drivers/<int:id>/edit/", driver_update, name="driver_update"),
    path("drivers/<int:id>/delete/", driver_delete, name="driver_delete"),
]
