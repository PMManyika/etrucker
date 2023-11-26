from accounts.forms import UserProfileForm
from .models import Profile
from django.contrib import admin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    form = UserProfileForm
