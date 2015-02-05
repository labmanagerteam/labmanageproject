# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django import forms
from django.forms.formsets import formset_factory
from django.forms.formsets import BaseFormSet
from django.db import transaction
import django.utils.timezone as timezone

from labmanageproject.my_db import lab_db, open_lab, lab, open_lab_detail, user_order
from labmanageproject.my_filter import filter_result_dict_list, filter_result_tuple_list, \
    filter_result_dict_list_trans_date
from labmanageproject.my_exception import FormInValidError
from labmanageproject.my_field import my_date_field, my_time_field

UID = 'uid'
UNAME = 'uname'
LCID = 'lcid'
LCNAME = 'lcname'
LID = 'lid'
LNAME = 'lname'
OLNAME = 'olname'
OLID = 'olid'
DATE = 'date'
BEGIN_TIME = 'begin_time'
END_TIME = 'end_time'
BEGIN_DATE_TIME = 'begin_date_time'
END_DATE_TIME = 'end_date_time'
TYPE = 'type'
STATUS = open_lab.STATUS
ACCEPT = open_lab.ACCEPT
REFUSE = open_lab.REFUSE
LNUMBER = lab.LNUMBER
OLDID = open_lab_detail.OLDID
ORDER_ID = user_order.ORDER_ID


def add_open_lab(*args):
    error = [{'result': 'e'}]
    for a in args:
        if not a:
            return error

    olname = args[0]
    uid = args[1]
    lcid = args[2]
    lid = args[3]
    begin_time = args[4]
    end_time = args[5]

    if not lab_db.get_lab_center_by_lcid(lcid):
        print 'no that lcid'
        return error

    if len(lid) != len(begin_time) or len(lid) != len(end_time):
        print 'no the same length'
        return error

    s_lid = [a for (a, b) in lab_db.get_all_lab_by_lcid(lcid)]
    print s_lid
    for l in lid:
        if l not in s_lid:
            print 'no that lid'
            return error

    import datetime

    for i in xrange(len(begin_time)):
        try:
            begin_time[i] = timezone.make_aware(datetime.datetime.strptime(begin_time[i], '%Y-%m-%d %H'),
                                                timezone.get_current_timezone())
            end_time[i] = timezone.make_aware(datetime.datetime.strptime(end_time[i], '%Y-%m-%d %H'),
                                              timezone.get_current_timezone())
        except ValueError:
            print 'join error'
            return error

    index = 0
    join_list = []
    with transaction.atomic():
        for (l, b, e) in zip(lid, begin_time, end_time):
            if lab_db.get_checked_open_lab(l, b, e):
                join_list.append({'result': index})
            index += 1
        if join_list:
            return join_list
        else:
            begin_date_time = begin_time[0]
            for b in begin_time:
                if begin_date_time > b:
                    begin_date_time = b

            end_date_time = end_time[0]
            for e in end_time:
                if e > end_date_time:
                    end_date_time = e
            olid = uid + timezone.now().strftime('%Y %m %d %H %M %S')
            detail_list = [[l, b, e] for (l, b, e) in zip(lid, begin_time, end_time)]
            lab_db.add_open_lab(olid, lcid, olname, uid, begin_date_time, end_date_time, "单次", detail_list)
            return [{'result': 's'}]


def get_all_lab_center():
    m_filter = filter_result_dict_list([LCID, LCNAME])
    return m_filter(lab_db.get_all_lab_center())


def get_all_lab_by_lcid(lcid):
    m_filter = filter_result_dict_list([LID, LNAME])
    return m_filter(lab_db.get_all_lab_by_lcid(lcid))


filter_open_lab = filter_result_dict_list_trans_date([OLNAME, UNAME, LCNAME, TYPE,
                                                      BEGIN_DATE_TIME, END_DATE_TIME, OLID])

filter_open_lab_detail = filter_result_dict_list([LNAME, BEGIN_TIME, END_TIME, LNUMBER, OLDID])

filter_open_lab_detail_no_name = filter_result_dict_list([OLDID, OLID, LID, BEGIN_TIME, END_TIME, LNUMBER])

filter_lab = filter_result_dict_list([LID, LNAME, LCID, LNUMBER])

filter_user_order = filter_result_dict_list(user_order.NAME_LIST)


def get_all_unchecked_open_lab(begin_line_number, page_size):
    result = {
        'result': '',
        'uc_ol': []
    }
    uncheck_open_lab_list = lab_db.get_all_unchecked_open_lab(int(begin_line_number), int(page_size))
    if uncheck_open_lab_list:
        result['result'] = 'success'
        result['uc_ol'] = filter_open_lab(uncheck_open_lab_list)
    else:
        result['result'] = 'no_more'

    return result


def get_open_lab_by_olid(olid):
    return filter_open_lab(lab_db.get_open_lab(**{OLID: olid}))


def get_open_lab_detail_by_olid(olid, mtype):
    if mtype == u"单次":
        r = filter_open_lab_detail(lab_db.get_open_lab_detail(**{OLID: olid}))
        print "get_open_lab_detail_by_olid:%s" % r
        return r
    elif mtype == u"循环":
        pass
    else:
        return False


def get_conflict_open_lab(open_lab_detail):
    conflic_list = []
    for detail_line in open_lab_detail:
        [conflic_list.append(c) for c in
         filter_open_lab(lab_db.get_conflict_open_lab(detail_line[LNAME], detail_line[BEGIN_TIME],
                                                      detail_line[END_TIME], "未审核"))]

    print 'conflic_list:%s' % conflic_list

    return list(set(conflic_list))


def accept_open_lab(now_olid, conflict_list):
    with transaction.atomic():
        open_lab.update({STATUS: ACCEPT}, {OLID: now_olid})
        for conflict in conflict_list:
            open_lab.update({STATUS: REFUSE}, {OLID: conflict})

    return True


def refuse_open_lab(now_olid):
    open_lab.update({STATUS: REFUSE}, {OLID: now_olid})
    return True


def get_all_checked_open_lab(begin_line_number, page_size):
    r = filter_open_lab(lab_db.get_all_checked_open_lab(begin_line_number, page_size))
    return r


def do_user_order(oldid, uid):
    with transaction.atomic():
        detail = filter_open_lab_detail_no_name(lab_db.get_open_lab_detail_by_oldid(oldid))[0]
        lab = filter_lab(lab_db.get_lab_by_lid(detail[LID]))[0]
        if int(lab[LNUMBER]) <= int(detail[LNUMBER]):
            return [False, "这个实验室已经预约完了"]
        else:
            lab_db.add_user_order(oldid, uid)
            return [True]


def check_order_condition(oldid, uid):
    return True


def get_my_open_lab(uid):
    return filter_open_lab(lab_db.get_open_lab(**{UID: uid}))


def get_unchecked_order_by_oldid(oldid):
    return filter_user_order(user_order.get(**{user_order.OLDID: oldid, user_order.STATE: user_order.WAIT}))


filter_order = filter_result_dict_list([OLID, OLDID, OLNAME, UID, ORDER_ID, UNAME, LNAME, LCNAME])
filter_open_lab_detail_table = filter_result_dict_list(open_lab_detail.NAME_LIST)


def get_my_unchecked_order(uid):
    return filter_order(lab_db.get_order_to_my_open_lab(uid))


def accept_order(order_id):
    with transaction.atomic():
        # user_order.get(**{ORDER_ID: order_id})
        oldid = filter_user_order(user_order.get(**{ORDER_ID: order_id}))[0][OLDID]
        # return {'result': 'error', 'msg': '该实验室已满'}
        open_lab_detail_one = filter_open_lab_detail_table(open_lab_detail.get(**{OLDID: oldid}))[0]
        now_number = int(open_lab_detail_one[LNUMBER])
        max_number = filter_lab(lab.get(**{LID: open_lab_detail_one[LID]}))[0][LNUMBER]
        if int(open_lab_detail_one[LNUMBER]) > int(max_number):
            return {'result': 'error', 'msg': '该实验室已满'}
        else:
            user_order.update({user_order.STATE: user_order.ACCEPT}, {user_order.ORDER_ID: order_id})
            open_lab_detail.update({LNUMBER: str(now_number + 1)}, {OLDID: open_lab_detail_one[OLDID]})
            return {'result': 'success', 'msg': '已经同意'}


def refuse_order(order_id):
    user_order.update({user_order.STATE: user_order.REFUSE}, {user_order.ORDER_ID: order_id})
    return {'result': 'success', 'msg': '已经成功拒绝'}


filter_today_order = filter_result_dict_list(['card_number', 'oldid', 'lid'])


def get_today_order():
    return filter_today_order(lab_db.get_today_order())
