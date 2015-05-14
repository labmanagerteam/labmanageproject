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
get_all_lc_center_admin_str = r'^managers'
set_semster_str = r'^set_semster'
open_lab_str = r'^open_lab'
my_order_str = r'^my_order'


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'labmanageproject.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^admin/', include(admin.site.urls)),

                       url(r'^test_db/$', test_db),
                       url(r'^$', login),
                       url(r'^logout/$', all_check(logout)),
                       url(open_lab_str + r'/$', all_check(open_lab)),
                       url(open_lab_str + r'/send_open_lab/$', all_check(send_open_lab)),
                       url(open_lab_str + r'/send_circle_open_lab/$', all_check(send_circle_open_lab_view)),
                       url(r'^get_lab_by_lcid/$', get_lab_by_lcid_view),
                       url(check_open_lab_str + r'/$', all_check(check_open_lab)),
                       url(check_open_lab_str + r'/get_uncheck_open_lab/$', all_check(get_uncheck_open_lab)),
                       url(check_open_lab_str + r'/detail/(.*)/$', all_check(get_detail_open_lab)),
                       url(check_open_lab_str + r'/accept/$', all_check(accept_open_lab_view)),
                       url(check_open_lab_str + r'/refuse/$', all_check(refuse_open_lab_view)),
                       url(order_open_lab_str + r"/$", all_check(order_open_lab_0_view)),
                       url(order_open_lab_str + r"/(\d+)/$", all_check(order_open_lab_view)),
                       url(order_open_lab_str + r'/detail/(.+)/$', all_check(order_open_lab_detail_view)),
                       url(order_open_lab_str + r'/order/$', all_check(order_view)),
                       url(order_open_lab_str + r'/order_circle/', all_check(order_circle_view)),
                       url(check_user_order + r'/$', all_check(check_user_order_view)),
                       url(check_user_order + r'/reflect/$', all_check(check_user_order_reflect_view)),
                       url(check_user_order + r'/circle_reflect/$', all_check(check_circle_order_reflect_view)),
                       url(my_open_lab + r'/$', all_check(my_open_lab_view)),
                       url(my_open_lab + r'/detail/(.+)/(.+)$', all_check(my_open_lab_detail_view)),
                       url(add_user + r'/$', all_check(add_user_view)),
                       url(add_user + r'/one_student/$', all_check(add_one_student_view)),
                       url(add_user + r'/student_list/$', all_check(add_student_list_view)),
                       url(add_user + r'/one_teacher/$', all_check(add_one_teacher_view)),
                       url(add_user + r'/teacher_list/$', all_check(add_teacher_list_view)),
                       url(add + '/$', all_check(add_view)),
                       url(add + '/one_lab/$', all_check(add_one_lab_view)),
                       url(add + '/one_lab_center/$', all_check(add_one_lab_center_view)),
                       url(add + '/one_department/$', all_check(add_one_department_view)),
                       url(add + '/lab_center_list/$', all_check(add_lab_center_list_view)),
                       url(add + '/lab_list/$', all_check(add_lab_list_view)),
                       url(add + '/department_list/$', all_check(add_department_list_view)),
                       url(add + '/admin_list/$', all_check(add_admin_list_view)),
                       url('^today_order/$', today_order_view),
                       url(get_all_lc_center_admin_str + '/$', all_check(get_all_lab_center_admin_view)),
                       url(get_all_lc_center_admin_str + '/add/$', all_check(add_one_admin_view)),
                       url(get_all_lc_center_admin_str + '/delete/$', all_check(delete_one_lab_center_admin_view)),
                       url(get_all_lc_center_admin_str + '/change_password/$', all_check(change_admin_password_view)),
                       url(get_all_lc_center_str + '/$', all_check(get_all_lab_center_view)),
                       url(get_all_lc_center_str + '/delete/$', all_check(delete_one_lab_center_view)),
                       url(get_all_lc_center_str + '/(.+)/$', all_check(get_one_lab_center_detail_view)),
                       url(get_all_lc_center_str + '/.+/delete/$', all_check(delete_one_lab_view)),
                       url(set_semster_str + '/$', all_check(set_semster_view)),
                       url(set_semster_str + '/do/$', all_check(do_set_semster_view)),
                       url(my_order_str + '/$', all_check(my_order_view)),
)

