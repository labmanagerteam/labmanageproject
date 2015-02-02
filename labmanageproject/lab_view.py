# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.shortcuts import render
from django.http.response import HttpResponse

import json

from labmanageproject.lab_manage import *
from labmanageproject.my_decorator import *


def get_uid(request):
    return request.session['my_user']['uid']


def open_lab(request):
    print "open_lab"
    if request.method == 'POST':
        lc_list = get_all_lab_center()
        print request.POST
    else:
        lc_list = get_all_lab_center()

    return render(request, "open_lab.html", locals())


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
    result = add_open_lab(olname, request.session['my_user']['uid'], lcid, lid, begin_time, end_time)
    return HttpResponse(json.dumps(result))


def check_open_lab(request):
    return render(request, "check_open_lab.html")


def get_uncheck_open_lab(request):
    print request.POST
    begin_line_number = request.POST.get('begin_line_number', [])
    page_size = request.POST.get('page_size', [])
    if not begin_line_number or not page_size:
        return HttpResponse(json.dumps({'result': 'e'}))
    else:
        return HttpResponse(json.dumps(get_all_unchecked_open_lab(begin_line_number, page_size)))


def get_detail_open_lab(request, olid):
    import labmanageproject

    this_open_lab = get_open_lab_by_olid(olid)[0]
    print "this_oben_lab:%s" % this_open_lab
    if not this_open_lab:
        return render(request, 'error.html', {'error': '不存在这个开放计划'})
    else:
        this_open_lab_detail = get_open_lab_detail_by_olid(olid, this_open_lab[TYPE])
        print "this_open_lab_detail:%s" % this_open_lab_detail
        conflict_open_lab = get_conflict_open_lab(this_open_lab_detail)
        print "conflict_open_lab:%s" % conflict_open_lab
        conflict_list = []
        for c in conflict_open_lab:
            if c[OLID] == olid:
                continue
            else:
                conflict_list.append({
                    'body': c,
                    'detail': get_open_lab_detail_by_olid(c[OLID], c[TYPE])
                })
        print "conflict_list: %s" % conflict_list
        return render(request, "check_open_lab_detail.html", locals())


NOW_OPEN_LAB = 'now_open_lab'
CONFLICT_LIST = 'conflict_list'


@check_post_form({NOW_OPEN_LAB, CONFLICT_LIST})
def accept_open_lab_view(request):
    post_list = request.POST
    if post_list[CONFLICT_LIST] == "No Conflict":
        conflict_list = []
    else:
        conflict_list = post_list[CONFLICT_LIST]
    accept_open_lab(post_list[NOW_OPEN_LAB], conflict_list)
    return HttpResponse(json.dumps({'result': 'ok'}))


@check_post_form({NOW_OPEN_LAB})
def refuse_open_lab_view(request):
    refuse_open_lab(request.POST[NOW_OPEN_LAB])
    return HttpResponse(json.dumps({'result': 'ok'}))


def order_open_lab_view(request, page_number):
    from labmanageproject.urls import order_open_lab_str

    page_size = 20
    now_r = get_all_checked_open_lab(page_number, page_size)
    print "now_r:%s" % now_r
    next_r = ""
    print "next:%s" % get_all_checked_open_lab(int(page_number) + page_size, page_size)
    if get_all_checked_open_lab(int(page_number) + page_size, page_size):
        next_r = "/" + order_open_lab_str + "/" + str(int(page_number) + 1)
    prev_r = ""
    if int(page_number):
        prev_r = "/" + order_open_lab_str + "/" + str(int(page_number) - 1)
    return render(request, "order_open_lab.html", locals())


def order_open_lab_detail_view(request, olid):
    this_open_lab = get_open_lab_by_olid(olid)[0]
    if not this_open_lab:
        return render(request, "error.html", {"error": '不存在这个开放计划'})

    this_open_lab_detail_list = get_open_lab_detail_by_olid(olid, this_open_lab[TYPE])
    return render(request, "order_open_lab_detail.html", locals())


@check_post_form({'oldid'})
def order_view(request):
    oldid = request.POST['oldid']
    uid = get_uid(request)
    if check_order_condition(oldid, uid):
        do_user_order(oldid, uid)
        return HttpResponse(json.dumps({'result': 'success'}))
    else:
        return HttpResponse(json.dumps({'result': 'error', 'msg': '你不符合预约此开放计划的条件'}))


def check_user_order_view(request):
    my_order_list = get_my_unchecked_order(get_uid(request))
    print "my_order_list: %s" % my_order_list
    extra = u'<td><input type="button" class="accept" value="同意"/><input type="button" class="refuse" value="拒绝"/></td>'
    return render(request, "check_user_order.html", locals())


@check_post_form({'action', 'order_id'})
def check_user_order_reflect_view(request):
    action = request.POST['action']
    order_id = request.POST['order_id']

    if action == 'accept':
        return HttpResponse(json.dumps(accept_order(order_id)))
    elif action == 'refuse':
        return HttpResponse(json.dumps(refuse_order(order_id)))
    else:
        raise Exception("check_user_order_reflect_view shold not in")


def my_open_lab_view(request):
    open_lab_list = get_my_open_lab(get_uid(request))
    return render(request, "my_open_lab.html", locals())


def my_open_lab_detail_view(request, olid):
    old_list = get_open_lab_detail_by_olid(olid)

    if old_list:
        for old in old_list:
            oldid = old[OLDID]
            oldid['ordered'] = get_unchecked_order_by_oldid(oldid)
            return render(request, )
    else:
        return render(request, "error.html", {'error': 'no the oldid'})