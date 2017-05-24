from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Item(models.Model):
    owner = models.ForeignKey('auth.User')
    completed = models.BooleanField(default=False)
    item_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)
    date_completed = models.DateTimeField(blank=False, null=True)


    def complete(self):
        self.date_completed = timezone.now()
        self.completed = True
        self.save()

    def __str__(self):
        return self.item_name
