
from django import forms
from .models import Store
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("item_name", "completed", "store")



class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ("store_name", "address")
