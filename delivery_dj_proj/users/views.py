from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from django.conf.urls import url, include
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import io
from rest_framework.parsers import JSONParser
from .serializers import MerchantSerializer, DriverSerializer
from .models import Merchant, Token,Driver
import uuid
from django.http import JsonResponse
from django.utils.crypto import get_random_string


# Create your views here.
@api_view(['POST'])
def register_merchant(request):
    if request.method == 'POST':
        merchant = MerchantSerializer(data=request.data)
        if merchant.is_valid():
            merchant.save()
            return Response("Done")
        return Response(merchant.errors)

@api_view(['POST'])
def register_driver(request,merch_id):
    if request.method == 'POST':
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
    if request.method == 'POST':
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
    if request.method == 'GET':
        drivers = Merchant.objects.get(pk=merch_id).driver_set.filter(is_auth=True)
        dictionaries = [driver.as_dict() for driver in drivers]
        return JsonResponse(dictionaries,safe=False)

