from django.db import models
from .product import Product
from .mobile_phone_additional import *

class MobilePhone(Product):
    screen_diagonal = models.FloatField()
    battery_capacity = models.IntegerField()
    resolution_main_camera = models.FloatField()
    maker = models.ForeignKey(Maker, on_delete=models.PROTECT, related_name='products')
    os = models.ForeignKey(OS, on_delete=models.PROTECT, related_name='products')
    ram = models.ForeignKey(RAM, on_delete=models.PROTECT, related_name='products')

    class Meta:
        db_table = 'mobile_phones'