from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['driver', 'merchant', 'content', 'total_price', 'delivery_location']