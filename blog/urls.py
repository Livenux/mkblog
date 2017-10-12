#!/usr/bin/env python3
#__coding:utf-8__

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]