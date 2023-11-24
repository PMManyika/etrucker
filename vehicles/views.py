# views.py

from django.shortcuts import render, redirect
from .models import Vehicle
from .forms import VehicleForm  # Make sure you have a VehicleForm in your forms.py


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, "vehicles/vehicle_list.html", {"vehicles": vehicles})


def vehicle_create(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("vehicle_list")
    return render(request, "vehicles/vehicle_form.html", {"form": form})


def vehicle_update(request, id):
    vehicle = Vehicle.objects.get(id=id)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if form.is_valid():
        form.save()
        return redirect("vehicle_list")
    return render(
        request, "vehicles/vehicle_form.html", {"form": form, "vehicle": vehicle}
    )


def vehicle_delete(request, id):
    vehicle = Vehicle.objects.get(id=id)
    if request.method == "POST":
        vehicle.delete()
        return redirect("vehicle_list")
    return render(request, "vehicles/vehicle_delete_confirm.html", {"vehicle": vehicle})
