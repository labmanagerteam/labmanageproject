# -*- coding: utf-8 -*-
from labmanageproject.user_view import *
from labmanageproject.test_db import test_db
from labmanageproject.lab_view import *

from django.conf.urls import patterns, include, url
# from django.conf.urls.static import static
from django.contrib import admin
# from django.conf import settings

admin.autodiscover()

check_open_lab_str = r"^check_open_lab"
order_open_lab_str = r"^order_open_lab"
check_user_order = r"^check_order"
my_open_lab = r"^my_open_lab"
add_user = r'^add_user'
add = r'^add'

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'labmanageproject.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^admin/', include(admin.site.urls)),

                       url(r'^test_db/$', test_db),
                       url(r'^$', login),
                       url(r'^logout/$', logout),
                       url(r'^open_lab/$', open_lab),
                       url(r'^send_open_lab/$', send_open_lab),
                       url(r'^get_lab_by_lcid/$', get_lab_by_lcid_view),
                       url(check_open_lab_str + r'/$', check_open_lab),
                       url(check_open_lab_str + r'/get_uncheck_open_lab/$', get_uncheck_open_lab),
                       url(check_open_lab_str + r'/detail/(.*)/$', get_detail_open_lab),
                       url(check_open_lab_str + r'/accept/$', accept_open_lab_view),
                       url(check_open_lab_str + r'/refuse/$', refuse_open_lab_view),
                       url(order_open_lab_str + r"/(\d+)/$", order_open_lab_view),
                       url(order_open_lab_str + r'/detail/(.+)/$', order_open_lab_detail_view),
                       url(order_open_lab_str + r'/order/$', order_view),
                       url(check_user_order + r'/$', check_user_order_view),
                       url(check_user_order + r'/reflect/$', check_user_order_reflect_view),
                       url(my_open_lab + r'/$', my_open_lab_view),
                       url(my_open_lab + r'/detail/(.+)$', my_open_lab_detail_view),
                       url(add_user + r'/$', add_user_view),
                       url(add_user + r'/one_student/$', add_one_student_view),
                       url(add_user + r'/student_list/$', add_student_list_view),
                       url(add_user + r'/one_teacher/$', add_one_teacher_view),
                       url(add_user + r'/teacher_list/$', add_teacher_list_view),
                       url(add + '/$', add_view),
                       url(add + '/one_lab/$', add_one_lab_view),
                       url(add + '/one_lab_center/$', add_one_lab_center_view),
                       url(add + '/one_department/$', add_one_department_view),
                       url(add + '/one_admin/$', add_one_admin_view),
                       url('^today_order/$', today_order_view)
)

