# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.shortcuts import render
from django.http.response import HttpResponse
import re
import json
from labmanageproject.user_manage import check_password

def check_perm(perm):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            for t in request.session['perm_list']:
                t = t['url']
                pattern = re.compile(r'^' + t + '*')
                if pattern.match(request.path):
                    return func(request, *args, **kwargs)
            else:
                return render(request, 'out_perm.html', locals())

        return wrapper

    return decorator


def check_logged(func):
    def wrapper(request, *args, **kwargs):
        session_key = ['uid', 'uname', 'perm_list', 'identity', 'password']
        for key in session_key:
            if key not in request.session:
                return render(request, "not_log.html", {'msg': "你没有登陆或登陆超时，请重新登陆"})

        if not check_password(request.session['uid'], request.session['password']):
            return render(request, "not_log.html", {'msg': "密码已经改变请重新改变"})

        return func(request, *args, **kwargs)

    return wrapper


def check_post_form(name_list):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.method != 'POST':
                return HttpResponse(json.dumps({'result': "the method is not post"}))
            else:
                for name in name_list:
                    if name not in request.POST:
                        return HttpResponse(json.dumps({'result': "left one attr" + name}))
                    if not request.POST[name]:
                        return HttpResponse(json.dumps({'result': name + " is blank"}))
                return func(request, *args, **kwargs)

        return wrapper

    return decorator
