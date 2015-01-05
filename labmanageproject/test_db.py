# -*- coding: utf-8 -*-
from labmanageproject.my_db import *
from django.shortcuts import render_to_response
import django.utils.timezone as timezone


def test_get_identity_id_by_name():
    print "test_get_group_id"
    print get_identity_id_by_name("student")
    print get_identity_id_by_name("teacher")
    print get_identity_id_by_name("administer")


def test_add_department():
    print "test_add_department"
    add_department("1", "软件学院")
    add_department("2", "物理系")
    add_department("3", "电子系")


def test_ud_add_stu():
    print "test_ud_add_stu"
    user_db.add_student("1", "吴礼蔚", "11223344", "2012级　本科", "1")
    user_db.add_student("2", "Peter", "11223344", "2011级　本科", "2")
    user_db.add_student("3", "Paul", "11223344", "2011级　本科", "3")


def test_ud_add_teacher():
    print "test_ld_add_teacher"
    user_db.add_teacher('4', 'Wolf', '11223344', '1')
    user_db.add_teacher('5', 'Wolf2', '11223344', '2')
    user_db.add_teacher('6', 'Wolf3', '11223344', '3')


def test_ud_add_administer():
    print "test_ud_add_administer"
    user_db.add_administer('7', 'Admin1', '11223344', '1')
    user_db.add_administer('8', 'Admin2', '11223344', '2')
    user_db.add_administer('9', 'Admin3', '11223344', '3')


def test_check_password():
    print "test_check_password"
    # print __debug__
    print user_db.check_password("1", "11223344")


def test_ld_add_lab_center():
    print "test_ld_add_lab_center"
    lab_db.add_lab_center("1", "A中心")
    lab_db.add_lab_center("2", "B中心")
    lab_db.add_lab_center("3", "C中心")


def test_ld_add_lab():
    print "test_ld_add_lab"
    lab_db.add_lab("1", "A实验室", "1")
    lab_db.add_lab("2", "B实验室", "1")
    lab_db.add_lab("3", "C实验室", "2")
    lab_db.add_lab("4", "D实验室", "2")
    lab_db.add_lab("5", "E实验室", "3")
    lab_db.add_lab("6", "F实验室", "3")
    lab_db.add_lab("7", "G实验室", "4")


def test_ld_get_all_lab_center():
    print "test_ld_get_all_lab_center"
    print lab_db.get_all_lab_center()


def test_ld_get_all_lab_by_lcid():
    print "test_ld_get_all_lab_by_lcid"
    print lab_db.get_all_lab_by_lcid("1")
    print lab_db.get_all_lab_by_lcid("2")
    print lab_db.get_all_lab_by_lcid("3")


def test_ld_add_open_lab():
    def to_local_time(year, month, day, hour=0, minute=0, second=0):
        return timezone.make_aware(timezone.datetime(year, month, day, hour, minute, second),
                                   timezone.get_current_timezone())

    print "test_ld_add_open_lab"
    begin_date_time = to_local_time(2014, 11, 21)
    end_date_time = to_local_time(2014, 12, 20)
    olid = "123455"
    detail_list = (('1', to_local_time(2014, 11, 24, 10), to_local_time(2014, 11, 24, 12)),
                   ('2', to_local_time(2014, 11, 27, 10), to_local_time(2014, 11, 24, 12)))
    lab_db.add_open_lab(olid, '1', '1', begin_date_time, end_date_time, detail_list)


def test_ld_open_lab_by_uid():
    print "test_ld_open_lab_by_uid"
    print lab_db.get_open_lab_by_uid('1')


def test_db(request):
    print "begin"
    test_get_identity_id_by_name()
    # test_add_department()
    # test_ud_add_stu()
    test_check_password()
    # test_ld_add_lab_center()
    # test_ld_add_lab()
    test_ld_get_all_lab_center()
    test_ld_get_all_lab_by_lcid()
    # test_ld_add_open_lab()
    test_ld_open_lab_by_uid()
    # test_ud_add_teacher()
    test_ud_add_administer()
    return render_to_response("test.html")