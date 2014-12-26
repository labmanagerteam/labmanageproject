# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render

from labmanageproject.my_user import check_user, get_perm_list, login_form
from labmanageproject.my_decorator import *
import labmanageproject.my_lab as lab


def login(request):
    # c = {}
    # c.update(csrf(request))
    login_error = False
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uname = check_user(cd['uid'], cd['password'])
            print uname
            if uname:
                uname = uname[0]['uname']
                perm_list = get_perm_list(cd['uid'])
                request.session['perm_list'] = perm_list
                request.session['uname'] = uname
                request.session['uid'] = cd['uid']
                return render(request, 'home.html', locals())
            else:
                login_error = True
    else:
        form = login_form()
    # return render_to_response('login.html', locals(), context_instance=RequestContext(request, c))
    return render(request, 'login.html', locals())


def home(request):
    return render(request, 'home.html', locals())


@check_logged
@check_perm('预约实验室')
def ask_open_lab(request):
    if request.method == 'POST':
        form = lab.ask_open_lab_form(request.POST)
        if form.is_valid():
            return render(request, 'success_submit.html', {'success_message': '成功预约了实验室，请等待管理员审核'})
    else:
        form = lab.ask_open_lab_form(initial={'uid': request.session['uid']})
    # print form.as_p()
    return render(request, 'ask_open_lab.html', locals())



