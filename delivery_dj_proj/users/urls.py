from django.urls import path,include, re_path
from . import views
from .views import CustomAuthToken

urlpatterns = [
    path('merchant/', include('users.merchant_urls')),
    path('driver/', include('users.driver_urls')),
    re_path(r'^login/(?P<usertype>(driver|merchant))$', CustomAuthToken.as_view()), 
]