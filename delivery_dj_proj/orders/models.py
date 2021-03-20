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

    def as_dict(self):
        return {
            'id' : self.id,
            'city': self.city,
            'street' : self.street,
            'building' : self.building,
            'floor' : self.floor,
            'receiver_full_name' : self.receiver_full_name,
            'receiver_phone_number' : self.receiver_phone_number
        }