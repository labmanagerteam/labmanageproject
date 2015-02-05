# -*- coding: utf-8 -*-
__author__ = 'wlw'
from django import forms

from labmanageproject.my_db import user_db, get_user_table, get_department_table, get_lab_center_table
from labmanageproject.error_code import *
from django.db import transaction
from labmanageproject.my_check import *
from labmanageproject.my_exception import *


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
        },
        {
            URL: '/add_user',
            PNAME: '添加用户'
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


def check_student(uid, did):
    check_no_uid(uid)
    check_department(did)


def add_student_list_action(student_list):
    NUM_UID = 0
    NUM_DID = 4

    num = 0
    try:
        with transaction.atomic():
            print "student_list: %s" % student_list
            for student in student_list:
                check_student(student[NUM_UID], student[NUM_DID])
                check_no_empty_in_list(student)
                check_distribute_number(student, 6)
                num += 1
            user_db.add_student_list(student_list)
    except MyBaseException, e:
        raise e
    except Exception, e:
        print e.message
        return [num, e.message]


def add_one_student_action(uid, uname, password, card_number, grade, did):
    if get_user_table(**{'uid': uid}):
        return HAVE_USR
    elif not get_department_table(**{'did': did}):
        return NO_THAT_DEPARTMENT

    user_db.add_student(uid, uname, password, card_number, grade, did)


def check_teacher(uid, lcid):
    check_no_uid(uid)
    check_lab_center(lcid)


def add_one_teacher_action(uid, uname, password, lcid, card_number):
    if get_user_table(**{'uid': uid}):
        return HAVE_USR
    elif not get_lab_center_table(**{'lcid': lcid}):
        return NO_THAT_LAB_CENTER
    user_db.add_teacher(uid, uname, password, lcid, card_number)


def add_teacher_list_action(teacher_list):
    NUM_UID = 0
    NUM_LCID = 4
    num = 0
    try:
        print "teacher_list:%s" % teacher_list
        with transaction.atomic():
            for teacher in teacher_list:
                check_teacher(teacher[NUM_UID], teacher[NUM_LCID])
                num += 1
                check_no_empty_in_list(teacher)
                check_distribute_number(teacher, 5)
            user_db.add_teacher_list(teacher_list)
    except MyBaseException, e:
        raise e
    except Exception, e:
        print e.message
        return [num, e.message]