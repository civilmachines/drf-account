from django.urls import path
from . import views


app_name = 'drf_account'

urlpatterns = [
    # ex: api/account/bank/show/
    path('bank/show/', views.ShowBankView.as_view(), name='Show Banks'),
    # ex: api/account/account/show/
    path('account/show/', views.ShowBankAccountView.as_view(), name='Show Bank Accounts'),
    # ex: api/account/account/add/
    path('account/add/', views.AddBankAccountView.as_view(), name='Add Bank Account'),
    # ex: api/account/debit/show/
    path('debit/show/', views.ShowDebitCardView.as_view(), name='Show Debit Card'),
    # ex: api/account/debit/add/
    path('debit/add/', views.AddDebitCardView.as_view(), name='Add Debit Card'),
    # ex: api/account/credit/show/
    path('credit/show/', views.ShowCreditCardView.as_view(), name='Show Credit Card'),
    # ex: api/account/credit/add/
    path('credit/add/', views.AddCreditCardView.as_view(), name='Add Credit Card'),
    # ex: api/account/account/update/pk/
    path('account/update/<int:pk>/', views.UpdateBankAccountView.as_view(), name='Update Bank Account'),
    # ex: api/account/debit/update/pk/
    path('debit/update/<int:pk>/', views.UpdateDebitCardView.as_view(), name='Update Debit Card'),
    # ex: api/account/credit/update/pk/
    path('credit/update/<int:pk>/', views.UpdateCreditCardView.as_view(), name='Update Credit Card'),
]
