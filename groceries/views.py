from django.shortcuts import render
from django.utils import timezone
from .models import Item
from django.shortcuts import render, get_object_or_404


def item_list(request):
    items = Item.objects.filter(date_added__lte=timezone.now()).order_by('date_added')
    return render(request, 'groceries/item_list.html', {'items': items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'groceries/item_detail.html', {'item': item})
