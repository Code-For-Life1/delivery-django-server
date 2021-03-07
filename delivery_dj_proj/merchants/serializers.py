from rest_framework import serializers
from .models import Merchant

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ['firstname', 'lastname', 'company_name', 'company_address','phone_number']
