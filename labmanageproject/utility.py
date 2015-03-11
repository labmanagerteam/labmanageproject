# -*- coding: utf-8 -*-
__author__ = 'wlw'


def get_post(request, name_list):
    value_list = []
    for name in name_list:
        value_list.append(request.POST[name])
    return value_list


def create_json_return(d):
    import json
    from django.http.response import HttpResponse

    return HttpResponse(json.dumps(d))


success_response = create_json_return({'result': 'success'})


def create_error_response(d):
    r = {'result': 'error'}

    for (a, b) in d.items():
        r[a] = b

    return create_json_return(r)


def create_local_date(a):
    import django.utils.timezone as timezone

    return timezone.make_aware(a, timezone.get_current_timezone())


def list_to_integer_list(l):
    r = []
    for t in l:
        r.append(int(t))

    return r


from datetime import timedelta

one_day = timedelta(days=1)
one_week = timedelta(days=7)


def to_unique(l, count_func=None):
    if not count_func:
        for t in l:
            if l.count(t) > 1:
                del l[l.index(t)]
    else:
        for t in l:
            if count_func(t, l) > 1:
                del l[l.index(t)]
    return l