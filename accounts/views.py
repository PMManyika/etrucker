from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserUpdateForm
from .forms import UserProfileForm
from .models import Profile


@login_required
def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "accounts/profile.html", {"form": form})


@login_required
def update_profile(request):
    # Check if user already has first name and last name
    if request.user.first_name and request.user.last_name:
        return redirect(
            "expense_list"
        )  # Replace 'home' with the name of your home page URL

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("expense_list")  # Redirect after successful update
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "accounts/update_profile.html", {"form": form})


def custom_logout(request):
    logout(request)
    return redirect("/")
