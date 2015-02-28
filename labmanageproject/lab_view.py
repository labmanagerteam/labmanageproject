# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.shortcuts import render
from django.http.response import HttpResponse

import json

from labmanageproject.lab_manage import *
from labmanageproject.my_decorator import *
from labmanageproject.semster_action import get_max_week, get_now_week
from labmanageproject.utility import *
from labmanageproject.error_code import *

def get_uid(request):
    return request.session['my_user']['uid']


def open_lab(request):
    print "open_lab"
    if request.method == 'POST':
        lc_list = get_all_lab_center()
        print request.POST
    else:
        lc_list = get_all_lab_center()

    week_list = []
    a = get_now_week(request)

    if a:
        b = get_max_week()
        for t in xrange(a, b + 1):
            week_list.append(t)

    return render(request, "open_lab.html", locals())


def get_lab_by_lcid_view(request):
    lcid = request.GET['lcid']
    lab_dict = get_all_lab_by_lcid(lcid)
    print json.dumps(lab_dict)
    return HttpResponse(json.dumps(lab_dict))


@check_logged
@check_perm
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

    this_open_lab = get_open_lab_by_olid(olid)
    print "this_oben_lab:%s" % this_open_lab
    if not this_open_lab:
        return render(request, 'error.html', {'error': '不存在这个开放计划'})
    else:
        this_open_lab = this_open_lab[0]
        this_open_lab_detail = get_open_lab_detail_by_olid(olid, this_open_lab[TYPE])
        change_open_lab_detail = get_open_lab_detail_by_olid(olid, u"单次")
        print "this_open_lab_detail:%s" % this_open_lab_detail

        conflict_open_lab = get_conflict_open_lab(change_open_lab_detail)

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


def order_open_lab_0_view(request):
    return order_open_lab_view(request, '0')


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
    try:
        if check_order_condition(oldid, uid):
            do_user_order(oldid, uid)
            return HttpResponse(json.dumps({'result': 'success'}))
        else:
            return HttpResponse(json.dumps({'result': 'error', 'msg': '你不符合预约此开放计划的条件'}))
    except Exception, e:
        return create_error_response({'msg': e.message})


@check_post_form({'coldid'})
def order_circle_view(request):
    coldid = request.POST['coldid']
    uid = get_uid(request)
    try:
        do_user_circle_order(coldid, uid)
        return success_response
    except Exception, e:
        return create_error_response({'msg': e.message})

def check_user_order_view(request):
    uid = get_uid(request)
    my_order_list = get_my_unchecked_order(uid)
    print "my_order_list: %s" % my_order_list
    my_order_list = join_list(my_order_list, get_my_unchecked_circle_order(uid))
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


@check_post_form(['action', 'corder_id'])
def check_circle_order_reflect_view(request):
    [action, corder_id] = get_post(request, ['action', 'corder_id'])

    try:
        if action == 'accept':
            accept_circle_order(corder_id)
        elif action == 'refuse':
            refuse_circle_order(corder_id)
        else:
            raise Exception("check_user_order_reflect_view shold not in")
        print "return success"
        return success_response
    except Exception, e:
        return create_error_response({'msg': e.message})


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


def today_order_view(request):
    return HttpResponse(json.dumps(get_today_order()))


@check_post_form(['olname', 'lcid', 'begin_week_number', 'end_week_number'])
def send_circle_open_lab_view(request):
    [olname, lcid, begin_week_number, end_week_number] = get_post(request, ['olname', 'lcid', 'begin_week_number',
                                                                            'end_week_number'])

    base_name_list = ['lid', 'weekday', 'begin_time', 'end_time']
    val_list = []
    for n in base_name_list:
        t = request.POST.getlist(n, '[]')
        if not t:
            return create_error_response({'msg': "%s not can be empty" % n})
        else:
            val_list.append(t)
    [lid_list, weekday_list, begin_time_list, end_time_list] = val_list
    print "val_list:%s " % val_list

    try:
        open_circle_open_lab_action(olname, lcid, begin_week_number, end_week_number,
                                    lid_list, weekday_list, begin_time_list, end_time_list, get_uid(request))
        return success_response
    except JoinTimeListException, e:
        return create_error_response({'join_list': e.join_time_list})
    except MyListException, e:
        return create_error_response({'msg': generate_error_message(e.error_code, e.num)})
    except MyBaseException, e:
        return create_error_response({'msg': generate_error_message(e.error_code)})
    except Exception, e:
        return create_error_response({'msg': e.message})