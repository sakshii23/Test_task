from django import forms
from .models import Expense, ExpenseSplit
from django.forms import inlineformset_factory

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount']

ExpenseSplitFormSet = inlineformset_factory(Expense, ExpenseSplit, fields=['user', 'amount'], extra=1)
