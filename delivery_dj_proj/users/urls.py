from django.urls import path,include
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('merchant/', include('users.merchant_urls')),
    path('driver/', include('users.driver_urls')),
    path('login', obtain_auth_token), #This view is modified to return the id also
]