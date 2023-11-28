from accounts.forms import UserProfileForm, CompanyForm
from .models import Profile, Company
from django.contrib import admin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    form = UserProfileForm


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("user", "name")
    form = CompanyForm
