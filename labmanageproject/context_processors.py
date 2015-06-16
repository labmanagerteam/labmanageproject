# -*- coding: utf-8 -*-
__author__ = 'wlw'
from labmanageproject.semster_action import get_now_week


def my_user_proc(request):
    def now_week():
        a = get_now_week(request)
        if a:
            return '第%s周' % (str(a))
        else:
            return False

    if 'my_user' not in request.session:
        return {}
    else:
        my_user = request.session['my_user']
        return {
            'perm_list': my_user['perm_list'],
            'identity': my_user['identity'],
            'uname': my_user['uname'],
            'week': now_week(),
        }