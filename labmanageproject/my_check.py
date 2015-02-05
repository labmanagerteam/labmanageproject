# -*- coding: utf-8 -*-
from labmanageproject.my_exception import *
from labmanageproject.my_db import *
from labmanageproject.error_code import *

__author__ = 'wlw'

error_to_message = {
    'uid': '用户名为空',
    'password': '密码为空',

}


def check_post(request):
    if request.method != 'POST':
        raise NotPostException


def check_form_field(request, field_name_list):
    for field in field_name_list:
        if field not in request.POST:
            raise NotFillFieldError(error_to_message[field])


def check_no_uid(uid):
    if get_user_table(**{'uid': uid}):
        raise MyBaseException(HAVE_USR)


def check_lab_center(lcid):
    if not get_lab_center_table(**{'lcid': lcid}):
        raise MyBaseException(NO_THAT_LAB_CENTER)


def check_department(did):
    if not get_department_table(**{'did': did}):
        raise MyBaseException(NO_THAT_DEPARTMENT)


def check_no_empty_in_list(l):
    for a in l:
        if not a:
            raise MyBaseException(HAVE_EMPTY)


def check_distribute_number(l, num):
    if len(l) != num:
        raise MyBaseException(LEFT_DISTRIBUTE)