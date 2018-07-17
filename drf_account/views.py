from rest_framework.generics import CreateAPIView, ListAPIView


def get_bank_by_name(name):
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
    from .serializers import ShowBankAccountSerializer
    from .models import BankAccount

    serializer_class = ShowBankAccountSerializer
    queryset = BankAccount.objects.all()


class AddDebitCardView(CreateAPIView):
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
    from .serializers import ShowDebitCardSerializer
    from .models import DebitCard

    serializer_class = ShowDebitCardSerializer
    queryset = DebitCard.objects.all()


class AddCreditCardView(AddDebitCardView):
    from .serializers import AddCreditCardSerializer

    serializer_class = AddCreditCardSerializer


class ShowCreditCardView(ListAPIView):
    from .serializers import ShowCreditCardSerializer
    from .models import CreditCard

    serializer_class = ShowCreditCardSerializer
    queryset = CreditCard.objects.all()


class ShowBankView(ListAPIView):
    from .serializers import ShowBankSerializer
    from .models import BankMaster
    from django_filters.rest_framework.backends import DjangoFilterBackend

    serializer_class = ShowBankSerializer
    queryset = BankMaster.objects.all()
    filter_backends = (DjangoFilterBackend, )
