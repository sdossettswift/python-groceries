from django.conf.urls import url
from . import views
from views import StoreIndexView
from views import StoreDetailView
from views import ItemIndexView
from views import ItemDetailView
from views import StoreItemList
from views import StoreCreate


app_name = 'groceries'
#urlpatterns = [
        #url(r'^$', views.to_do_list, name='to_do_list'),
        #url(r'^item/(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
        #url(r'^item/new/$', views.item_new, name='item_new'),
        #url(r'^item/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
        #url(r'^stores$', views.store_list, name='store_list'),
        #url(r'^store/(?P<pk>\d+)/$', views.store_detail, name='store_detail'),
        #url(r'^store/new/$', views.store_new, name='store_new'),
        #url(r'^store/(?P<pk>\d+)/edit/$', views.store_edit, name='store_edit'),
        #url(r'^items$', views.item_list, name='item_list'),
        #url(r'^item/(?P<pk>\d+)/complete/$', views.complete_item, name='complete_item'),
        #url(r'^item/(?P<pk>\d+)/buy_again/$', views.buy_again, name='buy_again'),
#]

urlpatterns = [
        url(r'^$', StoreIndexView.as_view()),
        url(r'^stores/$', StoreIndexView.as_view(), name="store_index"),
        url(r'^stores/(?P<pk>\d+)/$', StoreDetailView.as_view(), name="store_detail"),
        url(r'^items/$', ItemIndexView.as_view(), name="favorite_groceries"),
        url(r'^items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name="item_detail"), 
        url(r'^stores/<?P<pk>\d/items/$', StoreItemList.as_view(), name="store_item_list"),
        # url(r'^/$', ViewClass.as_view(), name=""), 
        url(r'^store/new/$', StoreCreate.as_view(), name='store_create'),
        ]
