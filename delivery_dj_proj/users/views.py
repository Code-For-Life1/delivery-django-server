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
import uuid,json
from django.http import JsonResponse

# Create your views here.
@api_view(['POST'])
def register_merchant(request):
    if request.method == 'POST':
        serializer = MerchantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Done")
        return Response(serializer.errors)

@api_view(['POST'])
def register_driver(request,merch_id):
    if request.method == 'POST':
        serializer = DriverSerializer(data=request.data)
        merchant = Merchant.objects.get(pk=merch_id)
        if serializer.is_valid():
            driver = serializer.save(merchant)
            Token.objects.create(merchant=merchant,driver=driver)
            return Response("Done")
        return Response(serializer.errors)

@api_view(['POST'])
def authenticate_driver(request):
    if request.method == 'POST':
        driv_token = request.data['token']
        token = uuid.UUID(driv_token)
        try:
            token = Token.objects.get(pk=token)
        except:
            return Response("Invalid Token")
        driver = token.driver
        driver.is_auth = True
        driver.save()
        return Response("Done")

@api_view(['GET'])
def send_drivers(request,merch_id):
    if request.method == 'GET':
        drivers = Merchant.objects.get(pk=merch_id).driver_set.filter(is_auth=True)
        dictionaries = [driver.as_dict() for driver in drivers]
        jsonfile = json.dumps(dictionaries)
        return JsonResponse(dictionaries,safe=False)
