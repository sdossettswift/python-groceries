from django.shortcuts import render, redirect,  get_object_or_404
from django.utils import timezone
from .models import Item
from .forms import ItemForm
from .models import Store
from .forms import StoreForm


def store_list(request):
    stores = Store.objects.all()
    return render(request, 'groceries/store_list.html', {'stores': stores})


def item_list(request):
    items = Item.objects.filter(
        date_added__lte=timezone.now()).order_by('date_added')
    return render(request, 'groceries/item_list.html', {'items': items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'groceries/item_detail.html', {'item': item})


def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'groceries/store_detail.html', {'store': store})


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
    return render(request, 'groceries/item_new.html', {'form': form})


def store_new(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.save()
            return redirect('store_detail', pk=store.pk)
    else:
        form = StoreForm()
    return render(request, 'groceries/store_edit.html', {'form': form})


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)

        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            if item.completed:
                item.complete()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'groceries/item_edit.html', {'form': form})


def store_edit(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == "POST":
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            store = form.save(commit=False)
            store.save()
            return redirect('store_detail', pk=store.pk)
    else:
        form = StoreForm(instance=store)
    return render(request, 'groceries/store_edit.html', {'form': form})


def to_do_list(request):
    stores = Store.objects.all()
    items = Store.item_set
    return render(request, 'groceries/to_do_list.html', {
            'stores': stores, 'items': items})
