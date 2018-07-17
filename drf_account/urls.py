from django.urls import path
from . import views


app_name = 'drf_account'

urlpatterns = [
    path('bank/show/', views.ShowBankView.as_view(), name='Show Banks'),
    path('account/show/', views.ShowBankAccountView.as_view(), name='Show Bank Accounts'),
    path('account/add/', views.AddBankAccountView.as_view(), name='Add Bank Account'),
    path('debit/show/', views.ShowDebitCardView.as_view(), name='Show Debit Card'),
    path('debit/add/', views.AddDebitCardView.as_view(), name='Add Debit Card'),
    path('credit/show/', views.ShowCreditCardView.as_view(), name='Show Credit Card'),
    path('credit/add/', views.AddCreditCardView.as_view(), name='Add Credit Card'),
]
