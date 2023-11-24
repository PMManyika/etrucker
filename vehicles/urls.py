from django.urls import path
from . import views

urlpatterns = [
    path("vehicles/", views.vehicle_list, name="vehicle_list"),
    path("vehicles/new/", views.vehicle_create, name="vehicle_create"),
    path("vehicles/<int:id>/edit/", views.vehicle_update, name="vehicle_update"),
    path("vehicles/<int:id>/delete/", views.vehicle_delete, name="vehicle_delete"),
]
