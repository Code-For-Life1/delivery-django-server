import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class User(AbstractUser):
    username = None
    is_merchant = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'phone_number'

    objects = CustomUserManager()



class Merchant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100,default='')
    company_address = models.CharField(max_length=100,default='')

    def get_phone_number(self):
        return self.user.phone_number



class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    merchant = models.ManyToManyField(Merchant)

    def get_phone_number(self):
        return self.user.phone_number


    def as_dict(self):
        return {
            'first_name': self.user.first_name,
            'last_name' : self.user.last_name,
            'phone_number' : self.user.phone_number
        }



class UnauthDriver(models.Model):
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    def as_dict(self):
        return {
            'first_name': self.first_name,
            'last_name' : self.last_name,
            'phone_number' : self.phone_number,
            'merchant' : self.merchant
        }

    def __str__(self):
        return str(self.token)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)