from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from users.models import Driver
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def send_orders(request,driver_id):
    if request.method == 'GET':
        orders = Driver.objects.get(pk=driver_id).order_set.filter(is_done=False)
        dictionaries = [order.as_dict() for order in orders]
        return JsonResponse(dictionaries,safe=False)        
