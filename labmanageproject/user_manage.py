# -*- coding: utf-8 -*-
__author__ = 'wlw'
from django import forms

from labmanageproject.my_db import user_db, get_user_table, get_department_table, get_lab_center_table
from labmanageproject.error_code import *
from django.db import transaction
from labmanageproject.my_check import *
from labmanageproject.my_exception import *
from labmanageproject.my_filter import *


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
            URL: '/order_open_lab',
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

    super_admin_perm = [
        {
            URL: '/add',
            PNAME: '添加'
        },
        {
            URL: '/get_all_lab_center_admin',
            PNAME: '管理中心管理员'
        },
        {
            URL: '/get_all_lab_center',
            PNAME: '管理所有实验中心'
        },
        {
            URL: '/set_semster',
            PNAME: '设置学期起止时间'
        }
    ]

    identity_list = []
    perm_list = []
    if user_db.is_student(uid):
        perm_list = student_perm
        identity_list.append('学生')
    else:
        perm_list = []
        if user_db.is_teacher(uid):
            identity_list.append('教师')
            for p in teacher_perm:
                perm_list.append(p)

        if user_db.is_administer(uid):
            identity_list.append('实验室管理员')
            for p in administer_perm:
                perm_list.append(p)

        if uid == '0':
            identity_list.append('超级管理员')
            for p in super_admin_perm:
                perm_list.append(p)

    perm_list.append({'url': '/logout', 'pname': '退出'})
    return [perm_list, identity_list]


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


def add_one_teacher_action(uid, uname, password, lcid, card_number, is_admin):
    if get_user_table(**{'uid': uid}):
        return HAVE_USR
    elif not get_lab_center_table(**{'lcid': lcid}):
        return NO_THAT_LAB_CENTER
    user_db.add_teacher(uid, uname, password, lcid, card_number, is_admin)


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


def add_list_factory(do_function, check_function):
    def add_list(to_add_list):
        num = 0
        try:
            with transaction.atomic():
                for t in to_add_list:
                    check_function(t, num)
                    num += 1
                do_function(to_add_list)
        except MyListException, e:
            raise e
        except Exception, e:
            print e.message
            raise e

    return add_list


def check_lab_center_one_item(one_item, num):
    check_no_empty_in_list(one_item, num)
    if lab_center.get(**{'lcid': one_item[0]}):
        raise MyListException(HAVE_LAB_CENTER, num)


add_lab_center_list_action = add_list_factory(lab_center.add_list, check_lab_center_one_item)


def check_lab_one_item(one_item, num):
    check_no_empty_in_list(one_item, num)
    check_lab_center(one_item[2], num)
    if lab.get(**{'lid': one_item[0]}):
        raise MyListException(HAVE_LAB, num)


add_lab_list_action = add_list_factory(lab.add_list, check_lab_one_item)


def check_department_oneitem(oneitem, num):
    check_no_empty_in_list(oneitem, num)
    if department.get(**{'did': oneitem[0]}):
        raise MyListException(HAVE_DEPARTMENT, num)


add_department_list_action = add_list_factory(department.add_list, check_department_oneitem)


def check_admin_oneitem(oneitem, num):
    check_no_empty_in_list(oneitem, num)
    check_no_uid(oneitem[0], num)
    check_lab_center(oneitem[4], num)


def add_admin_list(admin_l):
    with transaction.atomic():
        for admin in admin_l:
            add_one_teacher_action(admin[0], admin[1], admin[2], admin[4], admin[3], is_admin=True)


add_admin_list_action = add_list_factory(add_admin_list, check_admin_oneitem)



def add_one_lab_action_action(lcid, lid, lname, lnumber):
    lab.add([lcid, lid, lname, lnumber])


def add_one_lab_center_action(lcid, lcname):
    lab_center.add([lcid, lcname])


def add_one_department_action(did, dname):
    department.add([did, dname])


def get_all_lab_center_admin_action():
    filter_in_this = filter_result_dict_list([user.UID, user.UNAME, user.CARD_NUMBER, lab_center.LCNAME])
    return filter_in_this(user_db.get_all_lab_center_admin())


def get_all_lab_center_action():
    lab_center_filter = filter_result_dict_list([lab_center.LCID, lab_center.LCNAME])
    return lab_center_filter(lab_db.get_all_lab_center())


def get_lab_by_lcid(lcid):
    lab_filter = filter_result_dict_list([lab.LID, lab.LNAME, lab.LNUMBER])
    return lab_filter(lab_db.get_all_lab_by_lcid(lcid))


def delete_one_admin_action(uid):
    with transaction.atomic():
        delete_administer_table({'uid': uid})
        delete_teacher_table({'uid': uid})
        user.delete({'uid': uid})


def delete_one_lab_center_action(lcid):
    with transaction.atomic():
        pass


def delete_one_lab_action(lid):
    pass


def change_password_action(uid, new_password):
    with transaction.atomic():
        check_uid(uid)
        user_db.change_password(uid, new_password)