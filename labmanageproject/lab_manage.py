# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django import forms

from labmanageproject.my_db import lab_db
from labmanageproject.my_filter import filter_result_dict_list


def get_all_lab_center():
    m_filter = filter_result_dict_list(['lcid', 'lcname'])
    return m_filter(lab_db.get_all_lab_center())


def get_all_lab_by_lcid(lcid):
    m_filter = filter_result_dict_list(['lid', 'lname'])
    return m_filter(lab_db.get_all_lab_by_lcid(lcid))