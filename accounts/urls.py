from django.urls import path
from . import views
from .views import update_profile, custom_logout

urlpatterns = [
    path("", update_profile, name="update_profile"),
    path("logout/", custom_logout, name="logout"),
]
