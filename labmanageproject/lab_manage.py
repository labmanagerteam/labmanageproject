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
from labmanageproject.my_check import *
from labmanageproject.semster_action import get_now_week, get_max_week
from labmanageproject.utility import *

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

    s_lid = [a for (a, b, c) in lab_db.get_all_lab_by_lcid(lcid)]
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

filter_open_lab_detail = filter_result_dict_list([LNAME, BEGIN_TIME, END_TIME, LNUMBER, OLDID, LID])

filter_open_lab_detail_no_name = filter_result_dict_list([OLDID, OLID, LID, BEGIN_TIME, END_TIME, LNUMBER])

filter_lab = filter_result_dict_list([LID, LNAME, LCID, LNUMBER])

filter_user_order = filter_result_dict_list(user_order.NAME_LIST)

filter_circle_open_lab_detail = filter_result_dict_list([lab.LNAME, circle_open_lab_detail.WEEKDAY,
                                                         circle_open_lab_detail.BEGIN_TIME,
                                                         circle_open_lab_detail.END_TIME,
                                                         lab.LNUMBER, circle_open_lab_detail.COLDID, LID])


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
        r = filter_circle_open_lab_detail(lab_db.get_circle_open_lab_detail(**{OLID: olid}))
        print "get_open_lab_detail_by_olid:%s" % r
        return r
    else:
        return False


def get_conflict_open_lab(open_lab_detail):
    conflic_list = []
    for detail_line in open_lab_detail:
        [conflic_list.append(c) for c in
         filter_open_lab(lab_db.get_conflict_open_lab(detail_line[LID], detail_line[BEGIN_TIME],
                                                      detail_line[END_TIME], "未审核"))]

    print 'conflic_list:%s' % conflic_list

    circle_conflict_list = []


    return list(set(conflic_list))


# def get_circle_conflict_open_lab(begin_time, end_time, detail_list):
# conflict_list = []
#     while begin_time < end_time:
#         for detail in detail_list:
#             t = begin_time
#             for i in xrange(0, int(detail_list[circle_open_lab_detail.WEEKDAY])):
#                 t += one_day
#             b_time = t
#             b_time.hour = detail[circle_open_lab_detail.BEGIN_TIME]
#             e_time = t
#             e_time.hour = detail[circle_open_lab_detail.END_TIME]
#             [conflict_list.append(c) for c
#              in lab_db.get_conflict_open_lab(detail[LID], create_local_date(b_time),
#                                              create_local_date(e_time), "未审核")]
#         begin_time += one_week


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


def open_circle_open_lab_action(olname, lcid, begin_week_number, end_week_number,
                                lid_list, weekday_list, begin_time_list, end_time_list, uid):
    from datetime import datetime

    if int(begin_week_number) >= int(end_week_number):
        raise Exception({'msg', "开始星期数比结束的大"})

    if int(end_week_number) > int(get_max_week()):
        raise Exception({'msg': "end_week_number greater then max"})

    if int(begin_week_number) < int(get_now_week()):
        raise Exception({'msg': "开始星期数在现在之前"})

    val_list = [lid_list, weekday_list, begin_time_list, end_time_list]

    for t1 in val_list:
        for t2 in val_list:
            if len(t1) != len(t2):
                raise Exception({'msg': 'not equal length'})

    weekday_list = list_to_integer_list(weekday_list)
    begin_time_list = list_to_integer_list(begin_time_list)
    end_time_list = list_to_integer_list(end_time_list)

    for w in weekday_list:
        if w < 0 or w > 6:
            raise Exception({'msg': 'error'})

    def check_time(l):
        for tt in l:
            if tt < 8 or tt > 22:
                raise Exception('time not in field')

    check_time(begin_time_list)
    check_time(end_time_list)

    for (a, b) in zip(begin_time_list, end_time_list):
        if a >= b:
            raise Exception({'msg': 'begin time greater end time'})

    check_lab_center(lcid)
    for lid in lid_list:
        check_lid(lid)

    olid = uid + timezone.now().strftime('%Y %m %d %H %M %S')

    detail_line_list = []
    for (lid, weekday, begin_time, end_time) in zip(lid_list, weekday_list, begin_time_list, end_time_list):
        detail_line_list.append([olid, lid, weekday, begin_time, end_time])

    OLID_INDEX = 0
    LID_INDEX = 1
    WEEKDAY_INDEX = 2
    BEGIN_TIME_INDEX = 3
    END_TIME_INDEX = 4

    datestring_format = '%Y-%m-%d %H:%M:%S'

    begin_date_time = semister.get_least_day_in_one_week(begin_week_number)
    end_date_time = semister.get_max_day_in_one_week(end_week_number) + one_day

    with transaction.atomic():

        join_time_list = []
        index = 1

        for detail in detail_line_list:
            for week_number in xrange(int(begin_week_number), int(end_week_number) + 1):
                date = semister.get_date(**{'week_number': week_number, 'weekday': detail[WEEKDAY_INDEX]})
                if not date:
                    raise Exception('It is not in the semister')
                date = date[0]
                begin_time = create_local_date(datetime(date.year, date.month, date.day, detail[BEGIN_TIME_INDEX]))
                end_time = create_local_date(datetime(date.year, date.month, date.day, detail[END_TIME_INDEX]))
                if lab_db.get_checked_open_lab(detail[LID_INDEX], begin_time, end_time):
                    join_time_list.append(index)
                    index += 1

        if join_time_list:
            raise JoinTimeListException(join_time_list)

        lab_db.add_circle_open_lab(olid, lcid, olname, uid, begin_date_time,
                                   end_date_time, detail_line_list)

        for detail in detail_line_list:
            for week_number in xrange(int(begin_week_number), int(end_week_number) + 1):
                date = semister.get_date(**{'week_number': week_number, 'weekday': detail[WEEKDAY_INDEX]})
                if not date:
                    raise Exception('It is not in the semister')
                date = date[0]
                begin_time = create_local_date(datetime(date.year, date.month, date.day, detail[BEGIN_TIME_INDEX]))
                end_time = create_local_date(datetime(date.year, date.month, date.day, detail[END_TIME_INDEX]))
                coldid = circle_open_lab_detail.get(**{OLID: olid,
                                                       LID: detail[LID_INDEX],
                                                       circle_open_lab_detail.WEEKDAY: detail[WEEKDAY_INDEX],
                                                       circle_open_lab_detail.BEGIN_TIME: detail[BEGIN_TIME_INDEX],
                                                       circle_open_lab_detail.END_TIME: detail[END_TIME_INDEX]})[0][0]
                open_lab_detail.add_one(olid, detail[LID_INDEX], begin_time, end_time, coldid)

