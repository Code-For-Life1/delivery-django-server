import io
import uuid

from django.conf.urls import include, url
from django.core import serializers
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Driver, Merchant, UnauthDriver
from .serializers import (MerchantSerializer, UnauthDriverSerializer,
                          UserSerializer)


# Create your views here.

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
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
        response['response'] = 'successfully registered new merchant.'
        response['phone_number'] = user.phone_number
        token = Token.objects.get(user=user).key
        response['token'] = token

        return JsonResponse(response,safe=False,status=status.HTTP_201_CREATED)

    return JsonResponse(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def merchant_add_driver(request):
    data = request.data

    data['merchant'] = request.user
    unauthdriver_serializer = UnauthDriverSerializer(data=data)

    if unauthdriver_serializer.is_valid():
        unauth_driver = unauthdriver_serializer.save()

        response = {}
        response['response'] = "Driver successfully added."
        response['first_name'] = unauth_driver.first_name
        response['last_name'] = unauth_driver.last_name
        response['phone_number'] = unauth_driver.phone_number

        return JsonResponse(response,safe=False,status=status.HTTP_201_CREATED)
        
    return JsonResponse(unauthdriver_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)



def is_valid_token(token): #helper function to use in checking the token and authenticating the driver
    token = uuid.UUID(token)
    unauth_driver = UnauthDriver.objects.get(pk=token)
    return unauth_driver

    

@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def check_token(request):
    token = request.data['token']
    try:
        is_valid_token(token)
    except:
        return JsonResponse({"response": "Invalid Token"}, safe=False, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"response": "Valid Token", "token" : token}, safe=False,status=status.HTTP_200_OK)



@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def authenticate_driver(request):
    driver_token = request.data['token']
    try:
        unauth_driver = is_valid_token(driver_token)
    except:
        return JsonResponse({"response": "Invalid Token"}, safe=False, status=status.HTTP_400_BAD_REQUEST)
    
    unauth_driver_data = unauth_driver.as_dict()
    data = {**unauth_driver_data, **request.data}
    data['is_driver'] = True
    data['is_merchant'] = False
    user_serializer = UserSerializer(data=data)

    if user_serializer.is_valid():
       
        user = user_serializer.save()
        driver = Driver.objects.create(user=user)
        driver.merchant.add(data['merchant'])
        
        response = {}
        response['response'] = 'successfully registered new driver.'
        response['first_name'] = unauth_driver.first_name
        response['last_name'] = unauth_driver.last_name
        response['phone_number'] = user.phone_number
        
        token = Token.objects.get(user=user).key #authentication Token
        response['token'] = token

        unauth_driver.delete()

        return JsonResponse(response,safe=False, status=status.HTTP_201_CREATED)

    return JsonResponse(user_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_drivers(request):
    if not request.user.is_merchant:
        return JsonResponse({"response" : "The user is not a merchant"}, safe=False, status=status.HTTP_400_BAD_REQUEST)

    merch_id = request.user.id
    drivers = Driver.objects.filter(merchant=merch_id)
    dictionaries = [driver.as_dict() for driver in drivers]
    return JsonResponse(dictionaries,safe=False, status=status.HTTP_200_OK)