from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$', views.item_list, name='item_list'),
        url(r'^item/(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
]
