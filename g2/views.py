from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView, ListView 
from .models import Store, Item

class StoreIndexView(generic.ListView):
    template_name = 'g2/store_index.html'
    context_object_name = 'store_index'
    
    def get_queryset(self):
        return Store.objects.all.order_by('-store_name')
    

class StoreDetailView(generic.DetailView):
    model = Store
    template_name = 'g2/store_detail.html'


class ItemIndexView(generic.ListView):
    template_name = 'g2/item_index.html'
    context_object_name = 'item_index'

    def get_queryset(self):
        return Item.objects.filter(
                date_added__lte=timezone.now()).order_by('date_added')


class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'g2/item_detail.html'


