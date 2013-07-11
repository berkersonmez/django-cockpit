from django.conf.urls import patterns, url

from cockpit import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page_id>\d+)/$', views.detail, name='detail'),
)