# -*- coding: utf-8 -*-
__author__ = 'wlw'

from labmanageproject.my_db import lab
from labmanageproject.my_filter import *
from labmanageproject.my_form import *
import django.utils.timezone as timezone
from django import forms


def get_date_time(date, time):
    return timezone.make_aware(timezone.datetime(date.year, date.month, date.day, time.hour, time.minute),
                               timezone.get_current_timezone())


def check_lab_not_open(data_dict):
    # print data_dict
    begin_date_time = get_date_time(data_dict['begin_date'], data_dict['begin_time'])
    end_date_time = get_date_time(data_dict['end_date'], data_dict['end_time'])
    value_dict = {
        lab.BEGIN_DATE_TIME: begin_date_time,
        lab.END_DATE_TIME: end_date_time,
        lab.EXAMINE_STATUS: lab.STATUS['accept'],
        lab.LAB_ID: data_dict['lab_id']
    }
    if lab.get_lab_open(filter_result_tuple_tuple(), value_dict):
        return True
    else:
        return False


def check_not_try_open_lab(data_dict):
    begin_date_time = get_date_time(data_dict['begin_date'], data_dict['begin_time'])
    end_date_time = get_date_time(data_dict['end_date'], data_dict['end_time'])
    value_dict = {
        lab.BEGIN_DATE_TIME: begin_date_time,
        lab.END_DATE_TIME: end_date_time,
        lab.UID: data_dict['uid'],
        lab.LAB_ID: data_dict['lab_id'],
        lab.EXAMINE_STATUS: lab.STATUS['wait']
    }
    if lab.get_lab_open(filter_result_tuple_tuple(), value_dict):
        # if lab.get_lab_open(filter_result_tuple_tuple(), begin_date_time, end_date_time):
        return True
    else:
        return False


def add_open_lab(data_dict):
    begin_date_time = get_date_time(data_dict['begin_date'], data_dict['begin_time'])
    end_date_time = get_date_time(data_dict['end_date'], data_dict['end_time'])
    value_dict = {
        lab.BEGIN_DATE_TIME: begin_date_time,
        lab.END_DATE_TIME: end_date_time,
        lab.UID: data_dict['uid'],
        lab.LAB_ID: data_dict['lab_id'],
        lab.EXAMINE_STATUS: lab.STATUS['wait']
    }
    lab.add_open_lab(value_dict)


class ask_open_lab_form(forms.Form):
    uid = forms.CharField(widget=forms.HiddenInput())
    lab_id = forms.ChoiceField(choices=lab.get_lab(filter_result_tuple_list()), label="实验室")
    begin_date = my_date_field(label="开始日期", error_messages={'required': "开始日期不能为空"})
    begin_time = forms.TimeField(label="开始时间", error_messages={'required': "开始时间", 'invalid': {"时间请按照　１４：３０　的格式"}})
    end_date = my_date_field(label="结束日期", error_messages={'required': "结束日期不能为空"})
    end_time = forms.TimeField(label="结束时间", error_messages={'required': "结束时间不能为空", 'invalid': {"时间请按照　１４：３０　的格式"}})

    def clean(self):
        clean_data = super(ask_open_lab_form, self).clean()
        if check_lab_not_open(clean_data):
            # print 1
            raise forms.ValidationError("该实验室在这时间段内已经开放了，你可以重新选择一个实验室，或者换个时间段")
        elif check_not_try_open_lab(clean_data):
            # print 2
            raise forms.ValidationError("你以前的申请与这次的申请想冲突，请先撤销以前的申请")
        else:
            try:
                add_open_lab(clean_data)
            except Exception, e:
                raise forms.ValidationError(e.message)
            return clean_data

