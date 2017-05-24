from django.shortcuts import render
from django.utils import timezone
from .models import Item


def item_list(request):
    items = Item.objects.filter(date_added__lte=timezone.now()).order_by('date_added')
    return render(request, 'groceries/item_list.html', {'items': items})

