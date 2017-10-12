#!/usr/bin/env python3
#__coding:utf-8__

from django.conf.urls import url

from . import views

aap_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]