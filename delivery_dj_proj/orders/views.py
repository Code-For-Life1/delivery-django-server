from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf.urls import url, include
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import io
from rest_framework.parsers import JSONParser
from orders.serializers import OrderSerializer

# Create your views here.
@api_view(['GET','POST'])
def receive_order(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Done")
        return Response(serializer.errors)
