from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
        # index - ex: /polls/
             # url(r'^$', views.index, name='index'),
        url(r'^$', views.IndexView.as_view(), name='index'),
        # detail - ex: /polls/5
        url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        # note: we are using primary key as opposed to question_id b/c we are using the default view
        # url(r'^(?P<question_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
            # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
        # results - ex: /polls/5/results
        url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
            # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
        # vote - ex: /polls/5/vote
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
            # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
        ]
