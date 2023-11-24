# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Driver
from .forms import (
    DriverForm,
)


@login_required
def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, "drivers/driver_list.html", {"drivers": drivers})


@login_required
def driver_create(request):
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.user = request.user  # Set the user to the currently logged in user
            driver.save()
            return redirect("driver_list")  # Redirect to the list of drivers
    else:
        form = DriverForm()

    return render(request, "drivers/driver_form.html", {"form": form})


@login_required
def driver_update(request, id):
    driver = Driver.objects.get(id=id)
    form = DriverForm(request.POST or None, instance=driver)
    if form.is_valid():
        form.save()
        return redirect("driver_list")
    return render(request, "drivers/driver_form.html", {"form": form, "driver": driver})


@login_required
def driver_delete(request, id):
    driver = Driver.objects.get(id=id)
    if request.method == "POST":
        driver.delete()
        return redirect("driver_list")
    return render(request, "drivers/driver_delete_confirm.html", {"driver": driver})
