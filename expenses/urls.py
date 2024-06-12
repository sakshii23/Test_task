from django.urls import path
from .views import share_expense, dashboard, friends_expenses

urlpatterns = [
    path('share/', share_expense, name='share_expense'),
    path('dashboard/', dashboard, name='dashboard'),
    path('friends/<int:friend_id>/', friends_expenses, name='friends_expenses'),
]
    