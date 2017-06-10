from django.conf.urls import url
from . import views

app_name ='g2'
urlpatterns = [
        #store urls: index, detail, form(add/edit/delete)
        #item urls: index, detail, form(add/edit/delete)
        #list of items by store
        #mark as purchased
        #mark to buy again
        url(r'^/items/$', views.ListView.as_view(), name='groceries_index'),
        url(r'^/stores/$', views.ListView.as_view(), name='store_index'),
        url(r'^/stores/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='store_detail'),
        url(r'^/items/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='item_detail'),
#        url(r'^/items/(?P<pk>[0-9]+)/buyagain/$', views.buy_again, name='buy_again'),
#        url(r'^/items/(?P<pk>[0-9]+)/purchase/$', views.purchase,  name='mark_as_bought'),
#        url(r'^/stores/(?P<pk>[0-9]+)/items/$', views.ListView.as_view(), name='list_by_store'),
        ]
