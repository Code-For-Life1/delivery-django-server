from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('driver/get/<int:driver_id>', views.send_orders),
    path('merchant/set_order', views.receive_order),
]
