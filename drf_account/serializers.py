from rest_framework import serializers


class AddBankAccountSerializer(serializers.ModelSerializer):
    bank = serializers.CharField(max_length=254, required=True, allow_null=False, allow_blank=False)

    class Meta:
        from .models import BankAccount
        model = BankAccount
        fields = ('nickname', 'bank', 'description', 'accnumber')


class ShowBankSerializer(serializers.ModelSerializer):

    class Meta:
        from .models import BankMaster
        model = BankMaster
        fields = ('name', 'bank_aliases')


class ShowBankAccountSerializer(serializers.ModelSerializer):
    bank = ShowBankSerializer(many=False)

    class Meta:
        from .models import BankAccount

        model = BankAccount
        fields = ('id', 'nickname', 'bank', 'description', 'accnumber', 'update_date', 'create_date')


class AddDebitCardSerializer(serializers.ModelSerializer):
    bank = serializers.CharField(max_length=254, required=True, allow_null=False, allow_blank=False)

    class Meta:
        from .models import DebitCard

        model = DebitCard
        fields = ('nickname', 'bank', 'description', 'account', 'vendor', 'free_atmtransaction',
                  'free_own_atmtransaction')


class ShowDebitCardSerializer(serializers.ModelSerializer):
    bank = ShowBankSerializer(many=False)
    account = ShowBankAccountSerializer(many=False)
    vendor = serializers.SerializerMethodField()

    @staticmethod
    def get_vendor(obj):
        return obj.get_vendor_display()

    class Meta:
        from .models import DebitCard

        model = DebitCard
        fields = ('id', 'nickname', 'bank', 'description', 'account', 'vendor', 'free_atmtransaction',
                  'free_own_atmtransaction', 'free_other_atmtransaction')


class AddCreditCardSerializer(serializers.ModelSerializer):
    bank = serializers.CharField(max_length=254, required=True, allow_null=False, allow_blank=False)

    class Meta:
        from .models import CreditCard

        model = CreditCard
        fields = ('nickname', 'bank', 'description', 'account', 'vendor', 'statement_date', 'limit', 'duedate_duration')


class ShowCreditCardSerializer(ShowDebitCardSerializer):

    class Meta:
        from .models import CreditCard

        model = CreditCard
        fields = ('id', 'nickname', 'bank', 'description', 'account', 'vendor', 'statement_date', 'limit',
                  'duedate_duration')
