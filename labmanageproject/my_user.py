# -*- coding: utf-8 -*-
__author__ = 'wlw'

from labmanageproject.my_db import get_user, get_uer_identity_perm, get_user_perm
from labmanageproject.my_filter import *
from django import forms


def check_user(uid, password):
    return get_user(filter_result_dict_list(['uname']), uid, password)


def union_perm_list(a, b):
    for t in b:
        a.append(t)

    f = lambda x, y: x if y in x else x + [y]
    a = reduce(f, [[], ] + a)

    return a


def get_perm_list(uid):
    # print identiy_list
    # perm = []
    # for t in identiy_list:
    # print t
    #     perm.append(t[0])
    # return perm

    identity_perm_list = get_uer_identity_perm(filter_result_dict_list(['pname', 'url']), uid)
    user_perm_list = get_user_perm(filter_result_dict_list(['pname', 'url']), uid)
    perm_list = union_perm_list(identity_perm_list, user_perm_list)
    return perm_list


class login_form(forms.Form):
    uid = forms.CharField(label="用户名", error_messages={'required': "用户名不能为空"})
    password = forms.CharField(widget=forms.PasswordInput(), label="密码", error_messages={'required': "密码不能为空"})
