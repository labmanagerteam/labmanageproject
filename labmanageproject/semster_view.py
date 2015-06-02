# -*- coding: utf-8 -*-
__author__ = 'wlw'

from labmanageproject.my_decorator import check_post_form
from labmanageproject.utility import *
from labmanageproject.semster_action import *

from django.shortcuts import render


@check_post_form(['begin_date', 'end_date'])
def do_set_semster_view(request):
    [begin_date, end_date] = get_post(request, ['begin_date', 'end_date'])
    try:
        set_semster_action(begin_date, end_date)
        return success_response
    except Exception, e:
        return create_error_response({'msg': e.message})


def set_semster_view(request):
    return render(request, "set_semster.html", locals())