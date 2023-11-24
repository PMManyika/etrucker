# urls.py

from django.urls import path
from drivers.views import driver_list, driver_create, driver_update, driver_delete

app_name = "drivers"  # Namespace for these URLs

urlpatterns = [
    path("", driver_list, name="driver_list"),
    path("new/", driver_create, name="driver_create"),
    path("<int:id>/edit/", driver_update, name="driver_update"),
    path("<int:id>/delete/", driver_delete, name="driver_delete"),
]
