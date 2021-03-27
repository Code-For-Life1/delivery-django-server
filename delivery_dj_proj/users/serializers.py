from rest_framework import serializers
from .models import User, Merchant, Driver


class UserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
    style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields =  ['first_name', 'last_name',
                'phone_number', 'password', 'password2', 'is_driver', 'is_merchant']
        extra_kwargs = {
        'password': {'write_only': True},
        }

    def save(self, is_driver=False, is_merchant=False):

        user = User(
        phone_number=self.validated_data['phone_number'],
        first_name=self.validated_data['first_name'],
        last_name=self.validated_data['last_name'],
        is_driver=self.validated_data['is_driver'],
        is_merchant=self.validated_data['is_merchant']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ['company_name', 'company_address']

    def save(self, user, **kwargs):
        merchant = Merchant.objects.create(user=user)
        return merchant


# class DriverSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'password',
#                   'first_name', 'last_name', 'phone_number']

#     def save(self, merchant, **kwargs):
#         user = super().save()
#         user.is_driver = True
#         user.save()
#         driver = Driver.objects.create(user=user)
#         driver.merchant.add(merchant)
#         return driver



