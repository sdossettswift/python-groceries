from django.shortcuts import render, redirect,  get_object_or_404
from django.utils import timezone
from .models import Item
from .forms import ItemForm


def item_list(request):
    items = Item.objects.filter(
        date_added__lte=timezone.now()).order_by('date_added')
    return render(request, 'groceries/item_list.html', {'items': items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'groceries/item_detail.html', {'item': item})


def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.date_added = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'groceries/item_edit.html', {'form': form})


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.date_added = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'groceries/item_edit.html', {'form': form})
