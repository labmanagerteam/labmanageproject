# -*- coding: utf-8 -*-
__author__ = 'wlw'


def my_user_proc(request):
    if 'my_user' not in request.session:
        return {}
    else:
        my_user = request.session['my_user']
        return {
            'perm_list': my_user['perm_list']
        }