from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Expense(models.Model):
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses_paid')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.payer} paid {self.amount} on {self.date}"

class ExpenseSplit(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='splits')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user} owes {self.amount} for {self.expense}"
