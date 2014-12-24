# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django import forms
from labmanageproject.my_db import get_lab


class my_data_field(forms.DateField):
    class my_data_input(forms.DateInput):
        format_key = 'DATE_INPUT_FORMATS'
        input_type = 'date'

    widget = my_data_input()


class login_form(forms.Form):
    uid = forms.CharField(label="用户名", error_messages={'required': "用户名不能为空"})
    password = forms.CharField(widget=forms.PasswordInput(), label="密码", error_messages={'required': "密码不能为空"})


class ask_open_lab_form(forms.Form):
    uid = forms.CharField(widget=forms.HiddenInput())
    lab_id = forms.ChoiceField(choices=get_lab(), label="实验室")
    begin_date = my_data_field(label="开始日期", error_messages={'required': "开始日期不能为空"})
    begin_time = forms.TimeField(label="开始时间", error_messages={'required': "开始时间", 'invalid': {"时间请按照　１４：３０　的格式"}})
    end_data = my_data_field(label="结束日期", error_messages={'required': "结束日期不能为空"})
    end_time = forms.TimeField(label="结束时间", error_messages={'required': "结束时间不能为空", 'invalid': {"时间请按照　１４：３０　的格式"}})


