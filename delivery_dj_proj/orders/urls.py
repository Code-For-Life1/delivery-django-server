from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('driver/<int:driver_id>', views.send_orders),
]
