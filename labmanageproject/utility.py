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