from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView


def get_bank_by_name(name):
    """
    This function checks if the bank exists in the database or not.
    Parameters
    ----------
    name: str

    Returns
    -------
    str
        The name of the bank if it exists otherwise None.
    Examples
    --------
    To check if 'Axis Bank' bank is already present in Database or not.
    >>> print(get_bank_by_name('Axis Bank'))
    Axis Bank
    To check if 'Central Bank' bank is already present in Database or not.
    >>> print(get_bank_by_name('Central Bank'))
    None
    """
    from .models import BankMaster
    bmall = BankMaster.objects.all()
    try:
        bmall = bmall.get(name=name)
    except BankMaster.DoesNotExist:
        regex = '"' + name + '"'
        bmall = bmall.filter(aliases__iregex=regex)
        if len(bmall) > 0:
            return bmall[0]
    else:
        return bmall


class AddBankAccountView(CreateAPIView):
    """
    This view will allow the user to add a new bank account.
    """
    from .serializers import AddBankAccountSerializer

    serializer_class = AddBankAccountSerializer

    def perform_create(self, serializer):
        from .models import BankMaster

        bank = serializer.validated_data['bank']
        bank_master = get_bank_by_name(bank)
        if not bank_master:
            bank_master = BankMaster()
            bank_master.name = bank
            bank_master.created_by = self.request.user
            bank_master.save()
        serializer.validated_data['bank'] = bank_master
        serializer.save(created_by=self.request.user)


class ShowBankAccountView(ListAPIView):
    """
    This view will show the list of all bank account details.
    """
    from .serializers import ShowBankAccountSerializer
    from .models import BankAccount

    serializer_class = ShowBankAccountSerializer
    queryset = BankAccount.objects.all().order_by('-create_date')


class AddDebitCardView(CreateAPIView):
    """
    This view will allow the user to add a new debit card.
    """
    from .serializers import AddDebitCardSerializer

    serializer_class = AddDebitCardSerializer

    def perform_create(self, serializer):
        from .models import BankMaster, BankAccount

        if 'account' in serializer.validated_data.keys():
            if serializer.validated_data['account']:
                account_obj = BankAccount.objects.get(pk=serializer.validated_data['account'])
                serializer.validated_data['bank'] = account_obj.bank
            else:
                bank = serializer.validated_data['bank']
                bank_master = get_bank_by_name(bank)
                if not bank_master:
                    bank_master = BankMaster()
                    bank_master.name = bank
                    bank_master.created_by = self.request.user
                    bank_master.save()
                serializer.validated_data['bank'] = bank_master
        else:
            bank = serializer.validated_data['bank']
            bank_master = get_bank_by_name(bank)
            if not bank_master:
                bank_master = BankMaster()
                bank_master.name = bank
                bank_master.created_by = self.request.user
                bank_master.save()
            serializer.validated_data['bank'] = bank_master

        serializer.save(created_by=self.request.user)


class ShowDebitCardView(ListAPIView):
    """
    This view will show the list of all debit cards.
    """
    from .serializers import ShowDebitCardSerializer
    from .models import DebitCard

    serializer_class = ShowDebitCardSerializer
    queryset = DebitCard.objects.all().order_by('-create_date')


class AddCreditCardView(AddDebitCardView):
    """
    This view will allow the user to add a new credit card.
    """
    from .serializers import AddCreditCardSerializer

    serializer_class = AddCreditCardSerializer


class ShowCreditCardView(ListAPIView):
    """
    This view will show the list of all credit cards.
    """
    from .serializers import ShowCreditCardSerializer
    from .models import CreditCard

    serializer_class = ShowCreditCardSerializer
    queryset = CreditCard.objects.all().order_by('-create_date')


class ShowBankView(ListAPIView):
    """
    This view will show the list of all the banks.
    """
    from .serializers import ShowBankSerializer
    from .models import BankMaster
    from django_filters.rest_framework.backends import DjangoFilterBackend

    serializer_class = ShowBankSerializer
    queryset = BankMaster.objects.all().order_by('-create_date')
    filter_backends = (DjangoFilterBackend, )


class UpdateBankAccountView(UpdateAPIView):
    """
    This view is to update bank account details.
    """
    from .models import BankAccount
    from .serializers import UpdateBankAccountSerializer
    from django_filters.rest_framework.backends import DjangoFilterBackend

    queryset = BankAccount.objects.all()
    serializer_class = UpdateBankAccountSerializer
    filter_backends = (DjangoFilterBackend, )


class UpdateDebitCardView(UpdateAPIView):
    """
    This view is to update debit card details.
    """
    from .models import DebitCard
    from .serializers import UpdateDebitCardSerializer
    from django_filters.rest_framework.backends import DjangoFilterBackend

    queryset = DebitCard.objects.all()
    serializer_class = UpdateDebitCardSerializer
    filter_backends = (DjangoFilterBackend, )


class UpdateCreditCardView(UpdateAPIView):
    """
    This view is to update Credit card details.
    """
    from .models import CreditCard
    from .serializers import UpdateCreditCardSerializer
    from django_filters.rest_framework.backends import DjangoFilterBackend
    from drfaddons.filters import IsOwnerFilterBackend

    queryset = CreditCard.objects.all()
    serializer_class = UpdateCreditCardSerializer
    filter_backends = (DjangoFilterBackend, IsOwnerFilterBackend)

