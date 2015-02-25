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


def check_no_uid(uid, num='false'):
    if num == 'false':
        if get_user_table(**{'uid': uid}):
            raise MyBaseException(HAVE_USR)
    else:
        if get_user_table(**{'uid': uid}):
            raise MyListException(HAVE_USR, num)


def check_uid(uid):
    if not get_user_table(**{'uid': uid}):
        raise MyBaseException()


def check_lab_center(lcid, num='false'):
    if num == 'false':
        if not get_lab_center_table(**{'lcid': lcid}):
            raise MyBaseException(NO_THAT_LAB_CENTER)
    else:
        if not get_lab_center_table(**{'lcid': lcid}):
            raise MyListException(NO_THAT_LAB_CENTER, num)


def check_department(did):
    if not get_department_table(**{'did': did}):
        raise MyBaseException(NO_THAT_DEPARTMENT)


def check_no_empty_in_list(l, num="false"):
    if num == 'false':
        for a in l:
            if not a:
                raise MyBaseException(HAVE_EMPTY)
    else:
        for a in l:
            if not a:
                raise MyListException(HAVE_EMPTY, num)


def check_distribute_number(l, num):
    if len(l) != num:
        raise MyBaseException(LEFT_DISTRIBUTE)