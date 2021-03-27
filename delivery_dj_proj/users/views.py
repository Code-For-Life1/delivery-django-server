import io
import uuid

from django.conf.urls import include, url
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Driver, Merchant, Token
from .serializers import UserSerializer,MerchantSerializer


# Create your views here.
@api_view(['POST'])
def register_merchant(request):
    data = request.data
    data['is_driver'] = False
    data['is_merchant'] = True
    user_serializer = UserSerializer(data=data)
    merchant_serializer = MerchantSerializer(data=data)
    if user_serializer.is_valid() and merchant_serializer.is_valid():
       
        user = user_serializer.save()
        merchant_serializer.save(user)
        
        response = {}
        response['response'] = 'successfully registered new user.'
        response['phone_number'] = user.phone_number
        response['id'] = user.id

        return JsonResponse(response,safe=False,status=status.HTTP_201_CREATED)

    return JsonResponse(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_driver(request,merch_id):
    request.data['username'] = request.data['phone_number']
    request.data['password'] = get_random_string(8)
    driver_serializer = DriverSerializer(data=request.data)
    merchant = Merchant.objects.get(pk=merch_id)
    if driver_serializer.is_valid():
        driver = driver_serializer.save(merchant)
        Token.objects.create(merchant=merchant,driver=driver)
        return Response("Done")
    return Response(driver_serializer.errors)

@api_view(['POST'])
def authenticate_driver(request):
    driv_token = request.data['token']
    try:
        token = uuid.UUID(driv_token)
        checked_token = Token.objects.get(pk=token)
    except:
        return Response("Invalid Token")
    driver = checked_token.driver
    driver.is_auth = True
    driver.save()
    return Response("Done")

@api_view(['GET'])
def send_drivers(request,merch_id):
    drivers = Merchant.objects.get(pk=merch_id).driver_set.filter(is_auth=True)
    dictionaries = [driver.as_dict() for driver in drivers]
    return JsonResponse(dictionaries,safe=False)

