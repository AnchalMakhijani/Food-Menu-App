from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.itemname

    itemname = models.CharField(max_length=200)
    itemdesc = models.CharField(max_length=200)
    itemprice = models. IntegerField()