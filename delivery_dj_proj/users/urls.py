from django.urls import path,include
from . import views

urlpatterns = [
    path('merchant', views.register_merchant),
    path('driver/<int:merch_id>', views.register_driver),
    path('auth_driver', views.authenticate_driver),
    path('<int:merch_id>', views.send_drivers)

]