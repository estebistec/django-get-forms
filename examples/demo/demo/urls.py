# -*- coding: utf-8 -*-


from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('',
    url(r'^$', 'demo.views.search', name='search'),
)
