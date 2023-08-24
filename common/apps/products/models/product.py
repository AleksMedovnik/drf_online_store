from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    info = models.TextField(blank=True) 
    price = models.FloatField(
        default=0,
        validators=[
            MaxValueValidator(1000000000.00),
            MinValueValidator(0)
        ]
    )
    color = models.ForeignKey('Color', on_delete=models.PROTECT)
    category = models.ForeignKey('categories.Category', on_delete=models.PROTECT)

    class Meta:
        abstract = True