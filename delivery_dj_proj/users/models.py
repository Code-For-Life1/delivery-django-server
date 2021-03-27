import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager

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



class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    merchant = models.ManyToManyField(Merchant)
    is_auth = models.BooleanField(default=False)

    def as_dict(self):
        return {
            'id' : self.user.id,
            'first_name': self.user.first_name,
            'last_name' : self.user.last_name,
            'phone_number' : self.user.phone_number
        }



class Token(models.Model):
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.token)
