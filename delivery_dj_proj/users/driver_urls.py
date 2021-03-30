from django.urls import path,include
from . import views

urlpatterns = [
    path('register', views.register_driver),
    path('check_token', views.check_token),
    path('auth_driver', views.authenticate_driver),
]