# views.py
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta, datetime
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from drivers.models import Driver
from drivers.forms import DriverForm


@login_required
def expense_list(request):
    current_date = timezone.now()
    start_of_current_day = current_date.replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    date_seven_days_ago = current_date - timedelta(days=7)
    first_day_of_month = current_date.replace(day=1)

    if request.user.is_superuser:
        # For superusers: aggregate and order expenses by user
        expenses = (
            Expense.objects.values("user__username")
            .annotate(total=Sum("amount"))
            .order_by("-total")
        )

        # Calculate totals for all users
        expenses_data = Expense.objects.all()
    else:
        # For regular users: show only their expenses
        expenses = Expense.objects.filter(user=request.user).order_by("-date")

        # Calculate totals for the logged-in user
        expenses_data = expenses

    # Calculate totals
    total_amount_today = (
        expenses_data.filter(date__gte=start_of_current_day).aggregate(
            total=Sum("amount")
        )["total"]
        or 0
    )
    total_amount_last_7_days = (
        expenses_data.filter(date__gte=date_seven_days_ago).aggregate(
            total=Sum("amount")
        )["total"]
        or 0
    )
    total_amount_last_month = (
        expenses_data.filter(date__gte=first_day_of_month).aggregate(
            total=Sum("amount")
        )["total"]
        or 0
    )
    total_amount_all_time = expenses_data.aggregate(total=Sum("amount"))["total"] or 0

    context = {
        "expenses": expenses,  # This might be a list or a queryset, depending on user type
        "total_amount_today": total_amount_today,
        "total_amount_last_7_days": total_amount_last_7_days,
        "total_amount_last_month": total_amount_last_month,
        "total_amount_all_time": total_amount_all_time,
    }
    template = "expenses/expense_list.html"
    return render(request, template, context)


@login_required
def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Set the user to the current user
            expense.save()
            return redirect("expense_list")
    else:
        form = ExpenseForm()

    return render(request, "expenses/expense_form.html", {"form": form})


@login_required
def expense_update(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = (
                request.user
            )  # Reset the user to the current user (optional based on your logic)
            expense.save()
            return redirect("expense_list")
    else:
        form = ExpenseForm(instance=expense)

    return render(
        request, "expenses/expense_form.html", {"form": form, "expense": expense}
    )


def expense_delete(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == "POST":
        expense.delete()
        return redirect("expense_list")
    return render(request, "expenses/expense_delete_confirm.html", {"expense": expense})
