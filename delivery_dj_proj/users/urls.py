from django.urls import path,include, re_path
from . import views
from .views import CustomAuthToken
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet




urlpatterns = [
    path('merchant/', include('users.merchant_urls')),
    path('driver/', include('users.driver_urls')),
    re_path(r'^login/(?P<usertype>(driver|merchant))$', CustomAuthToken.as_view()), 
    re_path(r'^fcm/add_device$', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),

]