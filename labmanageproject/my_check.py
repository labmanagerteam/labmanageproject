# -*- coding: utf-8 -*-
from labmanageproject.my_exception import *

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