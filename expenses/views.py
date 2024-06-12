from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense, ExpenseSplit , User
from .forms import ExpenseForm, ExpenseSplitFormSet

@login_required
def share_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        formset = ExpenseSplitFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            expense = form.save(commit=False)
            expense.payer = request.user
            expense.save()
            splits = formset.save(commit=False)
            for split in splits:
                split.expense = expense
                split.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
        formset = ExpenseSplitFormSet()
    return render(request, 'expenses/share_expense.html', {'form': form, 'formset': formset})

@login_required
def dashboard(request):
    user = request.user
    expenses_paid = user.expenses_paid.all()
    expenses_split = user.expensesplit_set.all()

    total_owed = sum(split.amount for split in expenses_split)
    total_owes = sum(expense.amount for expense in expenses_paid) - total_owed
    total_balance = total_owed - total_owes

    context = {
        'total_balance': total_balance,
        'total_owed': total_owed,
        'total_owes': total_owes,
        'expenses_paid': expenses_paid,
        'expenses_split': expenses_split,
    }
    return render(request, 'expenses/dashboard.html', context)

@login_required
def friends_expenses(request, friend_id):
    friend = User.objects.get(id=friend_id)
    expenses_paid = friend.expenses_paid.all()

    context = {
        'friend': friend,
        'expenses_paid': expenses_paid,
    }
    return render(request, 'expenses/friends_expenses.html', context)
