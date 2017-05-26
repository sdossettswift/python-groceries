
from django import forms
from .models import Store
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("item_name", "quantity", "notes", "completed", "store")



class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ("store_name", "store_notes", "address")
