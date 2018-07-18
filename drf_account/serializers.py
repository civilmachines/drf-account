from rest_framework import serializers


class AddBankAccountSerializer(serializers.ModelSerializer):
    """
    AddBankAccountSerializer is a model serializer
    that includes the attributes required for creating a new bank account.
    """
    bank = serializers.CharField(max_length=254, required=True, allow_null=False, allow_blank=False)

    class Meta:
        from .models import BankAccount
        model = BankAccount
        fields = ('nickname', 'bank', 'description', 'accnumber')


class ShowBankSerializer(serializers.ModelSerializer):
    """
    ShowBankSerializer is a model serializer that shows the attributes of the bank.
    """
    class Meta:
        from .models import BankMaster
        model = BankMaster
        fields = ('name', 'bank_aliases')


class ShowBankAccountSerializer(serializers.ModelSerializer):
    """
    ShowBankAccountSerializer is a model serializer that shows the attributes of the bank account.
    """
    bank = ShowBankSerializer(many=False)

    class Meta:
        from .models import BankAccount

        model = BankAccount
        fields = ('id', 'nickname', 'bank', 'description', 'accnumber', 'update_date', 'create_date')


class AddDebitCardSerializer(serializers.ModelSerializer):
    """
    AddDebitCardSerializer is a model serializer
    that includes the attributes required for creating a new debit card.
    """
    bank = serializers.CharField(max_length=254, required=True, allow_null=False, allow_blank=False)

    class Meta:
        from .models import DebitCard

        model = DebitCard
        fields = ('nickname', 'bank', 'description', 'account', 'vendor', 'free_atmtransaction',
                  'free_own_atmtransaction')


class ShowDebitCardSerializer(serializers.ModelSerializer):
    """
    ShowDebitCardSerializer is a model serializer that shows the attributes of the Debit Card.
    """
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
    """
    AddDebitCardSerializer is a model serializer
    that includes the attributes required for creating a new credit card.
    """
    bank = serializers.CharField(max_length=254, required=True, allow_null=False, allow_blank=False)

    class Meta:
        from .models import CreditCard

        model = CreditCard
        fields = ('nickname', 'bank', 'description', 'account', 'vendor', 'statement_date', 'limit', 'duedate_duration')


class ShowCreditCardSerializer(ShowDebitCardSerializer):
    """
    ShowCreditCardSerializer is a model serializer that shows the attributes of the Credit Card.
    """
    class Meta:
        from .models import CreditCard

        model = CreditCard
        fields = ('id', 'nickname', 'bank', 'description', 'account', 'vendor', 'statement_date', 'limit',
                  'duedate_duration')


class UpdateBankAccountSerializer(serializers.ModelSerializer):
    """
    UpdateBankAccountSerializer is a model serializer to update a bank account detail.
    """
    from .models import BankMaster

    nickname = serializers.CharField(required=False)
    bank = serializers.PrimaryKeyRelatedField(required=False, queryset=BankMaster.objects.all())
    description = serializers.CharField(required=False)
    accnumber = serializers.CharField(required=False)
    minbal = serializers.IntegerField(required=False)

    class Meta:
        from .models import BankAccount
        model = BankAccount
        fields = ('nickname', 'bank', 'description', 'accnumber', 'minbal')


class UpdateDebitCardSerializer(serializers.ModelSerializer):
    """
    UpdateDebitCardSerializer is a model serializer to update debit card details.
    """
    from .models import BankMaster

    nickname = serializers.CharField(required=False)
    bank = serializers.PrimaryKeyRelatedField(required=False, queryset=BankMaster.objects.all())
    description = serializers.CharField(required=False)
    account = serializers.CharField(required=False)
    vendor = serializers.CharField(required=False)
    free_atmtransaction = serializers.IntegerField(required=False)
    free_own_atmtransaction = serializers.IntegerField(required=False)

    class Meta:
        from .models import DebitCard
        model = DebitCard
        fields = ('nickname', 'bank', 'description', 'account', 'vendor', 'free_atmtransaction',
                  'free_own_atmtransaction')


class UpdateCreditCardSerializer(serializers.ModelSerializer):
    """
    UpdateCreditCardSerializer is a model serializer to update Credit card details.
    """
    from .models import BankMaster

    nickname = serializers.CharField(required=False)
    bank = serializers.PrimaryKeyRelatedField(required=False, queryset=BankMaster.objects.all())
    description = serializers.CharField(required=False)
    account = serializers.CharField(required=False)
    vendor = serializers.CharField(required=False)
    limit = serializers.DecimalField(required=False, max_digits=50, decimal_places=5)
    statement_date = serializers.IntegerField(required=False)
    duedate_duration = serializers.IntegerField(required=False)

    class Meta:
        from .models import CreditCard
        model = CreditCard
        fields = ('nickname', 'bank', 'description', 'account', 'vendor', 'statement_date', 'limit', 'duedate_duration')
