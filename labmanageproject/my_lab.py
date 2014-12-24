# -*- coding: utf-8 -*-
__author__ = 'wlw'

import labmanageproject.my_db as db
from labmanageproject.my_filter import *
from datetime import datetime


def check_lab_not_open(data_dict):
    def get_date_time(date, time):
        return datetime(date.year, date.month, date.day, time.hour, time.minute)

    print data_dict
    begin_date_time = get_date_time(data_dict['begin_date'], data_dict['begin_time'])
    end_date_time = get_date_time(data_dict['end_date'], data_dict['end_time'])
    if db.get_lab_open_insert_time(filter_result_tuple_tuple(), begin_date_time, end_date_time):
        return True
    else:
        return False
