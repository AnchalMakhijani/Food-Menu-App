from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.itemname

    itemname = models.CharField(max_length=200)
    itemdesc = models.CharField(max_length=200)
    itemprice = models. IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png",
    )
