# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.shortcuts import render
from django.http import HttpResponseRedirect

from labmanageproject.user_manage import *


def login(request):
    login_error = False
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uname = check_password(cd['uid'], cd['password'])
            # print uname
            if uname:
                perm_list = get_perm_list(cd['uid'])
                my_user = {
                    'perm_list': perm_list,
                    'uname': uname,
                    'uid': cd['uid']
                }
                request.session['my_user'] = my_user
                return render(request, 'home.html', locals())
            else:
                login_error = True
    else:
        form = login_form()
    # return render_to_response('login.html', locals(), context_instance=RequestContext(request, c))
    return render(request, 'login.html', locals())


def logout(request):
    del request.session['my_user']
    return HttpResponseRedirect('/')


def add_user_view(request):
    add_list = [
        {
            'val': '1',
            'name': 'student'
        },
        {
            'val': '2',
            'name': 'teacher'
        }
    ]
    return render(request, "add_user.html", locals())