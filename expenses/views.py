# views.py
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from drivers.models import Driver
from drivers.forms import DriverForm


@login_required
def expense_list(request):
    if request.user.is_superuser:
        # If the user is a superuser, show all expenses
        expenses = Expense.objects.all().order_by("-id")
    else:
        # Otherwise, show only expenses for the logged-in user
        expenses = Expense.objects.filter(user=request.user).order_by("-id")
    # Pagination
    paginator = Paginator(expenses, 10)  # Show 10 expenses per page
    page_number = request.GET.get("page")
    expenses = paginator.get_page(page_number)

    context = {
        "expenses": expenses,
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
