from django.db import models
from users.models import Merchant,Driver

# Create your models here.


class Order(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=80)
    building = models.CharField(max_length=50)
    floor = models.CharField(max_length=3)
    receiver_full_name = models.CharField(max_length=60)
    receiver_phone_number = models.CharField(max_length=20)
    is_done = models.BooleanField(default=False)
    is_recieved = models.BooleanField(default=False) #by driver
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def as_dict(self):
        return {
            'id' : self.id,
            'receiver_full_name' : self.receiver_full_name,
            'receiver_phone_number' : self.receiver_phone_number,
            'merchant_phone_number': self.merchant.get_phone_number(),
            'driver_phone_number': self.driver.get_phone_number(),
            'driver_name': self.driver.user.first_name + " " + self.driver.user.last_name,
            'status': self.status,
            'city': self.city,
            'street' : self.street,
            'building' : self.building,
            'floor' : self.floor
        }