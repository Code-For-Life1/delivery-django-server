from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from users.models import Driver,Merchant
from rest_framework.decorators import api_view
from .serializers import OrderSerializer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def send_orders(request,driver_id):
    if request.method == 'GET':
        orders = Driver.objects.get(pk=driver_id).order_set.filter(is_done=False)
        dictionaries = [order.as_dict() for order in orders]
        return JsonResponse(dictionaries,safe=False)        


@api_view(['POST'])
def receive_order(request):
    data = request.data
    order_serializer = OrderSerializer(data=data)
    if order_serializer.is_valid():
        driver = order_serializer.save()
        return Response("Done")
    return Response(order_serializer.errors)


@api_view(['PUT'])
def order_is_done(request, order_id):
    if Order.objects.filter(pk=order_id).exists():
        Order.objects.filter(pk=order_id).update(is_done=True)
        return Response("Done")
    return Response("Invalid Order")