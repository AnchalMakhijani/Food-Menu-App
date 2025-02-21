from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.itemname

    username = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    itemname = models.CharField(max_length=200)
    itemdesc = models.CharField(max_length=200)
    itemprice = models. IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png",
    )

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    