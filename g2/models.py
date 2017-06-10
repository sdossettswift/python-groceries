from __future__ import unicode_literals

from django.db import models
from django.utils import timezone 

class Store(models.Model):
    store_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40, null=True, blank=True)
    store_notes = models.TextField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.store_name


class Item(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    item_name = models.CharField(max_length=40)
    date_added = models.DateTimeField(default=timezone.now)
    date_purchased = models.DateTimeField(blank=False, null=True)
    quantity = models.IntegerField(null=True, blank=True)

    def purchase(self):
        self.date_purchased=timezone.now()
        self.completed = True 
        self.save()


    def __str__(self):
        return self.item_name

