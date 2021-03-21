from rest_framework import serializers
from .models import User,Merchant,Driver

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'phone_number']

    def save(self, **kwargs):
        user = super().save()
        user.is_merchant = True
        user.save()
        merchant = Merchant.objects.create(user=user)
        return merchant

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'phone_number']

    def save(self, merchant,**kwargs):
        user = super().save()
        user.is_driver = True
        user.save()
        driver = Driver.objects.create(user=user)
        driver.merchant.add(merchant)
        return driver