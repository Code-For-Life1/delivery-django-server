from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User, Driver, Merchant
from users.helpers import get_user_by_phone

from .models import Order
from .serializers import OrderSerializer
from fcm_django.models import FCMDevice


# Create your views here.


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_orders_driver(request, OrderStatus):
    if not request.user.is_driver:
        return JsonResponse({"response" : "The user is not a driver"}, safe=False, status=status.HTTP_400_BAD_REQUEST)
    driver_id = request.user.id
    is_done = False
    if(OrderStatus=='completed'):
         is_done = True
    orders = Order.objects.filter(driver=driver_id, is_done=is_done)
    dictionaries = [order.as_dict() for order in orders]
    return JsonResponse(dictionaries,safe=False, status=status.HTTP_200_OK)        

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_orders_merchant(request, OrderStatus):
    if not request.user.is_merchant:
        return JsonResponse({"response" : "The user is not a merchant"}, safe=False, status=status.HTTP_400_NOT_ACCEPTABLE)
    merch_id = request.user.id
    is_done = False
    if OrderStatus=='completed':
         is_done = True
    orders = Order.objects.filter(merchant=merch_id, is_done=is_done)
    dictionaries = [order.as_dict() for order in orders]
    return JsonResponse(dictionaries,safe=False, status=status.HTTP_200_OK)




@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def receive_order(request):
    if not request.user.is_merchant:
        return JsonResponse({"response" : "The user is not a merchant"}, safe=False, status=status.HTTP_400_BAD_REQUEST)

    merch_id = request.user.id
    data = request.data
    data['merchant'] = merch_id
    phone_number = data['driver']
    user = get_user_by_phone(phone_number)

    data['driver'] = user.id
    devices = FCMDevice.objects.filter(user=user.id, active=True)
    devices.send_message(title="New Order Recieved!", body= user.first_name + " assigned you a new order")

    order_serializer = OrderSerializer(data=data)
    if order_serializer.is_valid():
        order = order_serializer.save()

        response = {"response" : "Order successfully received"}
        response = {**response, **order.as_dict()}

        return JsonResponse(response, safe=False, status=status.HTTP_200_OK)
        
    return JsonResponse(order_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_is_done(request, order_id):
    if not Order.objects.filter(pk=order_id).exists():
        return JsonResponse({"response" : "Invalid order"}, safe=False, status=status.HTTP_400_BAD_REQUEST)

    orders = Order.objects.filter(pk=order_id)
    orders.update(is_done=True)
    user = orders.first().merchant.user
    devices = FCMDevice.objects.filter(user=user.id, active=True)
    devices.send_message(title="Order is done!", body= user.first_name + " delivered the order")

    return JsonResponse({"response" : "Order is done"}, safe=False, status=status.HTTP_200_OK)
