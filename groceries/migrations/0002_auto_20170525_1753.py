# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='date_completed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='groceries.Store'),
            preserve_default=False,
        ),
    ]
