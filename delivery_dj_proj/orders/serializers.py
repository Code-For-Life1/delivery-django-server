from rest_framework import serializers
from .models import Order
from users.models import Driver, Merchant

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['receiver_full_name','receiver_phone_number', 'street', 'building', 'city','floor','merchant','driver']
    


    