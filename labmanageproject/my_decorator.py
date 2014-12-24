# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.shortcuts import render
import re


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
        session_key = ['uid', 'uname', 'perm_list']
        for key in session_key:
            if key not in request.session:
                return render(request, "not_log.html")
        else:
            return func(request, *args, **kwargs)

    return wrapper
