# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django import forms
from django.forms.formsets import formset_factory
from django.forms.formsets import BaseFormSet
from django.db import transaction
import django.utils.timezone as timezone

from labmanageproject.my_db import lab_db, open_lab, lab, open_lab_detail
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

def get_all_lab_center():
    m_filter = filter_result_dict_list([LCID, LCNAME])
    return m_filter(lab_db.get_all_lab_center())


def get_all_lab_by_lcid(lcid):
    m_filter = filter_result_dict_list([LID, LNAME])
    return m_filter(lab_db.get_all_lab_by_lcid(lcid))


filter_open_lab = filter_result_dict_list_trans_date([OLNAME, UNAME, LCNAME, TYPE,
                                                      BEGIN_DATE_TIME, END_DATE_TIME, OLID])

filter_open_lab_detail = filter_result_dict_list([LNAME, BEGIN_TIME, END_TIME, LNUMBER, OLDID])


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