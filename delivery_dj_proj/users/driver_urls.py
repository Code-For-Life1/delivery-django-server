from django.urls import path,include
from . import views

urlpatterns = [
    path('register/<int:merch_id>', views.register_driver),
    path('auth_driver', views.authenticate_driver),
]