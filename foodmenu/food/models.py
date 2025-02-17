from django.db import models

# Create your models here.
class Item(models.Model):
    itemname = models.CharField(max_length=200)
    itemdesc = models.CharField(max_length=200)
    itemprice = models. IntegerField()