from django.urls import path,include
from . import views


urlpatterns = [
    path('register', views.merchant_add_driver),
    path('check_token', views.check_token),
    path('auth_driver', views.authenticate_driver),
]