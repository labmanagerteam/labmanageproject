# -*- coding: utf-8 -*-
__author__ = 'wlw'
from django import forms

from labmanageproject.my_db import user_db


class login_form(forms.Form):
    uid = forms.CharField(label="用户名", error_messages={'required': "用户名不能为空"})
    password = forms.CharField(widget=forms.PasswordInput(), label="密码", error_messages={'required': "密码不能为空"})


def check_password(uid, password):
    uname = user_db.check_password(uid, password)
    print uid
    print password
    if uname:
        return uname[0][0]
    else:
        return False


def get_perm_list(uid):
    URL = 'url'
    PNAME = 'pname'
    teacher_perm = [
        {
            URL: '/open_lab',
            PNAME: '开放实验室'
        },
        {
            URL: '/check_order',
            PNAME: '审核学生预约'
        },
        {
            URL: '/my_open_lab',
            PNAME: '我的开放计划'
        }
    ]
    student_perm = [
        {
            URL: '/order_open_lab/0/',
            PNAME: '预约实验室'
        }
    ]

    administer_perm = [
        {
            URL: '/check_open_lab',
            PNAME: '审核开放计划'
        }
    ]

    perm_list = []
    if user_db.is_student(uid):
        perm_list = student_perm
    else:
        perm_list = []
        if user_db.is_teacher(uid):
            for p in teacher_perm:
                perm_list.append(p)

        if user_db.is_administer(uid):
            for p in administer_perm:
                perm_list.append(p)

    perm_list.append({'url': '/logout', 'pname': '退出'})
    return perm_list

