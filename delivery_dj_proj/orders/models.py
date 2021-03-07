from django.db import models
from django.utils import timezone
import drivers.models
from drivers import models as drivers_models
from merchants import models as merchants_models



# Create your models here.

class Order(models.Model):
    driver = models.ForeignKey(drivers_models.Driver,on_delete=models.CASCADE)
    merchant = models.ForeignKey(merchants_models.Merchant,on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    total_price = models.FloatField()
    delivery_location = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    delivery_status = models.CharField(max_length=50,default="Pending")
    