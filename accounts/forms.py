from django import forms
from django.contrib.auth.models import User
from .models import Profile, Company


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["user", "role"]


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["user", "name"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
