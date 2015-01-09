# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.shortcuts import render
from django.http.response import HttpResponse

import json

from labmanageproject.lab_manage import *


def open_lab(request):
    print "open_lab"
    if request.method == 'POST':
        lc_list = get_all_lab_center()
        print request.POST
    else:
        lc_list = get_all_lab_center()

    return render(request, "open_lab.html", locals())


def open_lab2(request):
    print "open_lab"
    if request.method == 'POST':
        [form, formset] = open_lab_form_factory(False, **request.POST)
        if form.is_valid() and formset.is_valid():
            render(request, "success_submit.html", {'successs_message': "开放计划已提交，请等待管理员审核"})
    else:
        [form, formset] = open_lab_form_factory(True, uid=request.session['my_user']['uid'])

    return render(request, "open_lab2.html", locals())


def get_lab_by_lcid_view(request):
    lcid = request.GET['lcid']
    lab_dict = get_all_lab_by_lcid(lcid)
    print json.dumps(lab_dict)
    return HttpResponse(json.dumps(lab_dict))


def send_open_lab(request):
    print request.POST
    olname = request.POST.get('olname', [])
    lcid = request.POST.get('lcid', [])
    lid = request.POST.getlist('lid[]', [])
    begin_time = request.POST.getlist('begin_time[]', [])
    end_time = request.POST.getlist('end_time[]', [])
    result = check_open_lab(olname, request.session['my_user']['uid'], lcid, lid, begin_time, end_time)
    return HttpResponse(json.dumps(result))


def check_open_lab(request):
    pass