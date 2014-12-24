# -*- coding: utf-8 -*-
__author__ = 'wlw'

from labmanageproject.my_db import get_user, get_uer_identity_perm, get_user_perm

import re


def check_user(uid, password):
    return get_user(uid, password)


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

    identity_perm_list = get_uer_identity_perm(uid)
    user_perm_list = get_user_perm(uid)
    perm_list = union_perm_list(identity_perm_list, user_perm_list)
    return perm_list

