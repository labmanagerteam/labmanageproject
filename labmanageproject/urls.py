# -*- coding: utf-8 -*-
from labmanageproject.user_view import *
from labmanageproject.test_db import test_db
from labmanageproject.lab_view import *

from django.conf.urls import patterns, include, url
# from django.conf.urls.static import static
from django.contrib import admin
# from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'labmanageproject.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^admin/', include(admin.site.urls)),

                       url(r'^test_db/$', test_db),
                       url(r'^$', login),
                       url(r'^open_lab/$', open_lab),
                       url(r'^open_lab2/$', open_lab2),
                       url(r'^send_open_lab/$', send_open_lab),
                       url(r'^get_lab_by_lcid/$', get_lab_by_lcid_view),
                       url(r'^check_open_lab/$', check_open_lab),
)
