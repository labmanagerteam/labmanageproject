# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.db import connection, transaction
import exceptions


def do_sql(sql, param):
    cursor = connection.cursor()
    cursor.execute(sql, param)
    return cursor


def add_method(tname, name_list):
    sql = "insert into " + tname + "(" + name_list[0]
    value = "(%s"
    for name in name_list[1:len(name_list)]:
        sql += "," + name
        value += ",%s"
    value += ")"
    sql += ")" + "values" + value
    print sql

    def add(value_list):
        v_list = value_list[0]
        inner_sql = sql
        for v in value_list[1:len(value_list)]:
            v_list.append(v)
            inner_sql += "," + value
        print inner_sql
        print v_list
        do_sql(inner_sql, v_list)

    return add


def get_method(tname):
    sql = "select * from " + tname + " where "

    def get(**kwargs):
        inner_sql = sql
        v_list = []
        for (key, value) in kwargs.items():
            inner_sql += key + "=%s and"
            v_list.append(value)
        inner_sql += " 1=1"
        print inner_sql
        result = do_sql(inner_sql, v_list)
        return result.fetchall()

    return get

def get_department_id_by_name(dname):
    sql = "select gid from department where dname=%s"
    cursor = do_sql(sql, [dname])
    return cursor.fetchall()[0][0]


def get_card_number(uid):
    return "11223344"


def add_department(did, dname):
    sql = "insert into department(did,dname) values(%s,%s)"
    do_sql(sql, [did, dname])


add_user_table = add_method('user', ['uid', 'uname', 'password', 'card_number'])
add_teacher_table = add_method('teacher', ['uid', 'lcid'])
add_student_table = add_method('student', ['uid', 'did', 'grade'])
add_administer_table = add_method('administer', ['uid', 'lcid'])

get_user_table = get_method('user')
get_student_table = get_method('student')
get_teacher_table = get_method('teacher')
get_administer_table = get_method('administer')


class user_db():

    @staticmethod
    def add_student(uid, uname, password, grade, did):
        with transaction.atomic():
            sql = "insert into user(uid,uname,password,card_number) " \
                  "VALUES(%s,%s,%s,%s,%s)"
            do_sql(sql, [uid, uname, password, get_card_number(uid)])
            sql = "insert into student(uid,did,grade) values(%s,%s,%s)"
            do_sql(sql, [uid, did, grade])

    @staticmethod
    def add_student_list(student_list):
        pass

    @staticmethod
    def delete_student():
        pass

    @staticmethod
    def add_teacher(uid, uname, password, lcid):
        with transaction.atomic():
            sql = "insert into user(uid, uname, password, card_number)" \
                  "values(%s,%s,%s,%s,%s)"
            do_sql(sql, [uid, uname, password, get_card_number(uid)])
            sql = "insert into teacher(uid, lcid)" \
                  "values(%s,%s)"
            do_sql(sql, [uid, lcid])

    @staticmethod
    def add_teacher_list():
        pass

    @staticmethod
    def add_administer(uid, uname, password, lcid):
        with transaction.atomic():
            add_user_table([[uid, uname, password, get_card_number(uid)]])
            add_administer_table([[uid, lcid]])

    @staticmethod
    def check_password(uid, password):
        sql = "select uname from user where uid=%s and password = %s"
        cursor = do_sql(sql, [uid, password])
        result = cursor.fetchall()
        return result

    @staticmethod
    def is_student(uid):
        if get_student_table(uid=uid):
            return True
        else:
            return False

    @staticmethod
    def is_teacher(uid):
        if get_teacher_table(uid=uid):
            return True
        else:
            return False

    @staticmethod
    def is_administer(uid):
        if get_administer_table(uid=uid):
            return True
        else:
            return False

    def __init__(self):
        pass


class lab_db():
    @staticmethod
    def add_lab_center(lcid, lcname):
        sql = "insert into lab_center(lcid, lcname) values(%s,%s)"
        do_sql(sql, [lcid, lcname])

    @staticmethod
    def add_lab(lid, lname, lcid):
        sql = "insert into lab(lid, lname, lcid) values(%s,%s,%s)"
        do_sql(sql, [lid, lname, lcid])

    @staticmethod
    def delete_lab_by_lid(lid):
        sql = "delete from lab where lid = %s"
        do_sql(sql, lid)

    @staticmethod
    def get_all_lab_center():
        sql = "select lcid,lcname from lab_center"
        result = do_sql(sql, [])
        return result.fetchall()

    @staticmethod
    def get_all_lab_by_lcid(lcid):
        sql = "select lid,lname from lab where lcid=%s"
        result = do_sql(sql, [lcid])
        return result.fetchall()

    @staticmethod
    def add_open_lab(olid, lcid, olname, uid, begin_date_time, end_date_time, detail_list):
        with transaction.atomic():
            sql = "insert into open_lab(olid, lcid, olname, uid, begin_date_time, end_date_time)" \
                  "values(%s,%s,%s,%s,%s,%s)"
            do_sql(sql, [olid, lcid, olname, uid, begin_date_time, end_date_time])

            for detail in detail_list:
                sql = "insert into open_lab_detail(oldid, olid, lid, begin_time, end_time)" \
                      "values(NULL,%s,%s,%s,%s)"
                do_sql(sql, [olid, detail[0], detail[1], detail[2]])

    @staticmethod
    def get_open_lab_by_uid(uid):
        sql = "select * from open_lab where uid=%s"
        result = do_sql(sql, [uid])
        return result.fetchall()
