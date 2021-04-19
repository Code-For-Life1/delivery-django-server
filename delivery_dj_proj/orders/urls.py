from django.contrib import admin
from django.urls import path, re_path,include
from . import views

urlpatterns = [
    re_path(r'driver/get/(?P<OrderStatus>(new|completed))$', views.send_orders_driver),
    re_path(r'merchant/get/(?P<OrderStatus>(new|completed))$', views.send_orders_merchant),
    path('merchant/set_order', views.receive_order),
    path('driver/is_done/<int:order_id>', views.order_is_done)
]
