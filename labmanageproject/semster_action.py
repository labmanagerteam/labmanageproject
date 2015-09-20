# -*- coding: utf-8 -*-
__author__ = 'wlw'

from my_db import semister
from datetime import datetime
from datetime import timedelta

from labmanageproject.utility import create_local_date


def set_semster_action(begin_date, end_date):
    time_format = "%Y-%m-%d"
    begin_date = datetime.strptime(begin_date, time_format)
    end_date = datetime.strptime(end_date, time_format)

    if begin_date > end_date:
        raise Exception()

    if end_date < datetime.now():
        raise Exception()

    one_day = timedelta(days=1)
    now_week = 1
    now_date = begin_date

    r = []

    while now_date <= end_date:
        t = []
        t.append(create_local_date(now_date))
        t.append(now_week)
        t.append(now_date.weekday())
        r.append(t)

        if now_date.weekday() == 6:
            now_week += 1

        now_date += one_day

    print 'semister:%s' % r
    semister.add_list(r)


def get_now_week(request=""):
    now = datetime.now()
    now = create_local_date(datetime(now.year, now.month, now.day))
    r = semister.get(**{'date': now})
    if r:
        return r[0][1]
    else:
        return False


def get_max_week():
    return semister.get_max_week()
