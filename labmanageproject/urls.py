# -*- coding: utf-8 -*-
from labmanageproject.view import *
from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'labmanageproject.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^admin/', include(admin.site.urls)),

                       url(r'^login/$', login),
                       url(r'^home/$', home),
                       url(r'^ask_open_lab/$', ask_open_lab)
)
