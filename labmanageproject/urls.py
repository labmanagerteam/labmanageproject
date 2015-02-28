# -*- coding: utf-8 -*-
from labmanageproject.user_view import *
from labmanageproject.test_db import test_db
from labmanageproject.lab_view import *
from labmanageproject.semster_view import *

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
get_all_lc_center_str = r'^get_all_lab_center'
get_all_lc_center_admin_str = r'^get_all_lab_center_admin'
set_semster_str = r'^set_semster'
open_lab_str = r'^open_lab'

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'labmanageproject.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^admin/', include(admin.site.urls)),

                       url(r'^test_db/$', test_db),
                       url(r'^$', login),
                       url(r'^logout/$', logout),
                       url(open_lab_str + r'/$', open_lab),
                       url(r'^send_open_lab/$', send_open_lab),
                       url(open_lab_str + r'/send_circle_open_lab/$', send_circle_open_lab_view),
                       url(r'^get_lab_by_lcid/$', get_lab_by_lcid_view),
                       url(check_open_lab_str + r'/$', check_open_lab),
                       url(check_open_lab_str + r'/get_uncheck_open_lab/$', get_uncheck_open_lab),
                       url(check_open_lab_str + r'/detail/(.*)/$', get_detail_open_lab),
                       url(check_open_lab_str + r'/accept/$', accept_open_lab_view),
                       url(check_open_lab_str + r'/refuse/$', refuse_open_lab_view),
                       url(order_open_lab_str + r"/(\d+)/$", order_open_lab_view),
                       url(order_open_lab_str + r'/detail/(.+)/$', order_open_lab_detail_view),
                       url(order_open_lab_str + r'/order/$', order_view),
                       url(order_open_lab_str + r'/order_circle/', order_circle_view),
                       url(check_user_order + r'/$', check_user_order_view),
                       url(check_user_order + r'/reflect/$', check_user_order_reflect_view),
                       url(check_user_order + r'/circle_reflect/$', check_circle_order_reflect_view),
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
                       url(add + '/lab_center_list/$', add_lab_center_list_view),
                       url(add + '/lab_list/$', add_lab_list_view),
                       url(add + '/department_list/$', add_department_list_view),
                       url(add + '/admin_list/$', add_admin_list_view),
                       url('^today_order/$', today_order_view),
                       url(get_all_lc_center_admin_str + '/$', get_all_lab_center_admin_view),
                       url(get_all_lc_center_admin_str + '/delete/$', delete_one_lab_center_admin_view),
                       url(get_all_lc_center_admin_str + '/change_password/$', change_admin_password_view),
                       url(get_all_lc_center_str + '/$', get_all_lab_center_view),
                       url(get_all_lc_center_str + '/delete/$', delete_one_lab_center_view),
                       url(get_all_lc_center_str + '/(.+)/$', get_one_lab_center_detail_view),
                       url(get_all_lc_center_str + '/.+/delete/$', delete_one_lab_view),
                       url(set_semster_str + '/$', set_semster_view),
                       url(set_semster_str + '/do/$', do_set_semster_view),
)

