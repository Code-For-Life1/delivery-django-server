import io
import uuid
import environ

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

from rest_framework.authtoken.views import ObtainAuthToken
from twilio.rest import Client
from .models import generateOTP

# Twilio authentication
env = environ.Env()
environ.Env.read_env()
twilio_client = Client(env('TWILIO_ACCOUNT_SID'), env('TWILIO_AUTH_TOKEN'))

# Create your views here.

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, usertype,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.is_driver==False and usertype=="driver":
            return JsonResponse({"response" : "This user is not a driver"}, safe=False, status=status.HTTP_400_BAD_REQUEST)
        if user.is_merchant==False and usertype=="merchant":
            return JsonResponse({"response" : "This user is not a merchant"}, safe=False, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})






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

def sendSMS(unauth_driver): # helper function to send sms
    message = twilio_client.messages \
            .create(
                body="\nHello " + unauth_driver.first_name + " " + unauth_driver.last_name + \
                ", here is your sign up token: " + unauth_driver.token,
                from_="+12244343836",
                to="+961" + unauth_driver.phone_number
            )

def resendSMS(unauth_driver): # helper function to resend sms
    newToken = generateOTP()
    UnauthDriver.objects.filter(phone_number=unauth_driver.phone_number)\
        .update(token=newToken)
    unauth_driver.token = newToken
    sendSMS(unauth_driver)

def check_unauthdriver(phone_nb): # helper function to find if unauth driver exists
    unauthdriver = UnauthDriver.objects.filter(phone_number=phone_nb)
    dictionaries = [driver.as_dict() for driver in unauthdriver]
    if len(dictionaries) == 1:
        return unauthdriver
    else:
        return False        

def check_authdriver(phone_nb): # helper function to find if auth driver exists
    authdriver = User.objects.filter(phone_number=phone_nb, is_driver=1)
    dictionaries = [driver.as_dict() for driver in authdriver]
    if len(dictionaries) == 1:
        return authdriver
    else:
        return False 


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

        sendSMS(unauth_driver)

        return JsonResponse(response,safe=False,status=status.HTTP_201_CREATED)
        
    return JsonResponse(unauthdriver_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def resend_sms(request):
    data = request.data
    phone_nb = data['phone_number']
    driver = check_unauthdriver(phone_nb)
    if driver == False:
        return JsonResponse({'response': 'Driver has not been added by merchant', 'phone_number': phone_nb}, safe=False, status=status.HTTP_400_BAD_REQUEST)
    resendSMS(driver[0])
    return JsonResponse({'response': 'SMS has been resent!', 'driver': driver.first().toJSON()}, safe=False, status=status.HTTP_200_OK)


def is_valid_token(token): #helper function to use in checking the token and authenticating the driver
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