from django.shortcuts import render, redirect,  get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Item, Store
from .forms import ItemForm, StoreForm


# these are function based views, look into class based views
# template view, form view -- check these out
# base mixin -- **


class StoreIndexView(ListView):
    model = Store
    context_object_name = 'store_index'


class StoreDetailView(DetailView):
    context_object_name = 'store_detail'
    queryset = Store.objects.all()


class ItemIndexView(ListView):
    model = Item
    context_object_name = 'favorite_groceries'


class ItemDetailView(DetailView):
    context_object_name = 'item_detail'
    queryset = Item.objects.all()


class StoreDetailView(DetailView):
    context_object_name = 'item_detail'
    queryset = Item.objects.all()


class StoreItemList(ListView):
    template_name = 'stores/store_item_list.html'

    def get_queryset(self):
        self.store = get_object_or_404(Store, store_name=self.args[0])
        return Item.objects.filter(store=self.store)

class StoreCreate(CreateView):
    model = Store
    fields = ['store_name', 'address', 'store_notes' ]
    
    
