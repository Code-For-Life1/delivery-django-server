from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import Driver, Merchant

from .models import Order
from .serializers import OrderSerializer

# Create your views here.


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_orders_driver(request,driver_id):
    orders = Driver.objects.get(pk=driver_id).order_set.filter(is_done=False)
    dictionaries = [order.as_dict() for order in orders]
    return JsonResponse(dictionaries,safe=False)        

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_orders_merchant(request,merch_id):
    orders = Merchant.objects.get(pk=merch_id).order_set.filter(is_done=False)
    dictionaries = [order.as_dict() for order in orders]
    return JsonResponse(dictionaries,safe=False)      


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def receive_order(request):
    data = request.data
    order_serializer = OrderSerializer(data=data)
    if order_serializer.is_valid():
        driver = order_serializer.save()
        return Response("Done")
    return Response(order_serializer.errors)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_is_done(request, order_id):
    if Order.objects.filter(pk=order_id).exists():
        Order.objects.filter(pk=order_id).update(is_done=True)
        return Response("Done")
    return Response("Invalid Order")
