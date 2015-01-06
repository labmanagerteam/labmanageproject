# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.shortcuts import render
from django.http.response import HttpResponse

import json

from labmanageproject.lab_manage import *


def open_lab(request):
    print "open_lab"
    lc_list = get_all_lab_center()

    return render(request, "open_lab.html", locals())


def get_lab_by_lcid_view(request):
    lcid = request.GET['lcid']
    lab_dict = get_all_lab_by_lcid(lcid)
    print json.dumps(lab_dict)
    return HttpResponse(json.dumps(lab_dict))