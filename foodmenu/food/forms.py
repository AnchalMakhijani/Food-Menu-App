from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['itemname', 'itemdesc', 'itemprice', 'item_image']