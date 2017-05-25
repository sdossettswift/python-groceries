from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$', views.item_list, name='item_list'),
        url(r'^item/(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
        url(r'^item/new/$', views.item_new, name='item_new'),
        url(r'^item/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
        url(r'^stores$', views.store_list, name='store_list'),
        url(r'^store/(?P<pk>\d+)/$', views.store_detail, name='store_detail'),
        url(r'^store/new/$', views.store_new, name='store_new'),
        url(r'^store/(?P<pk>\d+)/edit/$', views.store_edit, name='store_edit'),
        url(r'^to_do_list$', views.to_do_list, name='to_do_list'),
]
