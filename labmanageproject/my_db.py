# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.db import connection, transaction
import exceptions


def do_sql(sql, param):
    cursor = connection.cursor()
    cursor.execute(sql, param)
    return cursor


def get_user(my_filter, uid, password):
    """dict_list_filter should use ['uname']"""
    print uid, password
    sql = "select uname from user where uid=%s and password = %s"
    cursor = do_sql(sql, [uid, password])
    result = cursor.fetchall()
    print result
    return my_filter(result)


def get_identity(my_filter, uid):
    """dict_list_filter should use ['identity']"""
    sql = "select i.gname from user_identity ui,identity i where ui.uid=%s and i.gid=ui.gid"
    cursor = do_sql(sql, [uid])
    return my_filter(cursor.fetchall())


def get_identity_id(my_filter, uid):
    """dict_list_filter should use ['gid']"""
    sql = "select ui.gid from user_identity ui where ui.uid=%s"
    cursor = do_sql(sql, [uid])
    return my_filter(cursor.fetchall())


def get_user_perm(my_filter, uid):
    """dict_list_filter should use ['pname', 'url']"""
    sql = "select p.pname,p.url from user_perm up,perm p where up.uid=%sand p.pid=up.pid"
    cursor = do_sql(sql, [uid])
    return my_filter(cursor.fetchall())


def get_uer_identity_perm(my_filter, uid):
    """dict_list_filter should use ['pname', 'url']"""
    sql = "select p.pname,p.url from identity_perm ip,user_identity ui,perm p where ui.uid=%s and ip.gid=ui.gid and p.pid=ip.pid"
    cursor = do_sql(sql, [uid])
    return my_filter(cursor.fetchall())


def get_identity_id_by_name(gname):
    sql = "select gid from identity where gname=%s"
    cursor = do_sql(sql, [gname])
    return cursor.fetchall()[0][0]


def get_department_id_by_name(dname):
    sql = "select gid from department where dname=%s"
    cursor = do_sql(sql, [dname])
    return cursor.fetchall()[0][0]


def get_card_number(uid):
    return "11223344"


def add_department(did, dname):
    sql = "insert into department(did,dname) values(%s,%s)"
    do_sql(sql, [did, dname])


class user_db():

    @staticmethod
    def add_student(uid, uname, password, grade, did):
        with transaction.atomic():
            gid = get_identity_id_by_name("student")
            sql = "insert into user(uid,uname,password,card_number) " \
                  "VALUES(%s,%s,%s,%s,%s)"
            do_sql(sql, [uid, uname, password, get_card_number(uid)])
            sql = "insert into student(uid,did,grade) values(%s,%s,%s)"
            do_sql(sql, [uid, did, grade])
            sql = "insert into user_identity(ugid, uid, gid)" \
                  "values(NULL, %s, %s)"
            do_sql(sql, [uid, get_identity_id_by_name('student')])

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
            sql = "insert into user_identity(ugid, uid, gid)" \
                  "values(NULL, %s, %s)"
            do_sql(sql, [uid, get_identity_id_by_name('teacher')])

    @staticmethod
    def add_teacher_list():
        pass

    @staticmethod
    def add_administer(uid, uname, password, lcid):
        with transaction.atomic():
            sql = "insert into user(uid, uname, password, card_number)" \
                  "values(%s,%s,%s,%s,%s)"
            do_sql(sql, [uid, uname, password, get_card_number(uid)])
            sql = "insert into teacher(uid, lcid)" \
                  "values(%s,%s)"
            do_sql(sql, [uid, lcid])
            sql = "insert into user_identity(ugid, uid, gid)" \
                  "values(NULL, %s, %s)"
            do_sql(sql, [uid, get_identity_id_by_name('administer')])


    @staticmethod
    def check_password(uid, password):
        sql = "select uname from user where uid=%s and password = %s"
        cursor = do_sql(sql, [uid, password])
        result = cursor.fetchall()
        return result[0][0]

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
        sql = "select * from lab_center"
        result = do_sql(sql, [])
        return result.fetchall()

    @staticmethod
    def get_all_lab_by_lcid(lcid):
        sql = "select lid,lname from lab where lcid=%s"
        result = do_sql(sql, [lcid])
        return result.fetchall()

    @staticmethod
    def add_open_lab(olid, lcid, uid, begin_date_time, end_date_time, detail_list):
        with transaction.atomic():
            sql = "insert into open_lab(olid, lcid, uid, begin_date_time, end_date_time)" \
                  "values(%s,%s,%s,%s,%s)"
            do_sql(sql, [olid, lcid, uid, begin_date_time, end_date_time])

            for detail in detail_list:
                sql = "insert into open_lab_detail(oldid, olid, lid, begin_time, end_time)" \
                      "values(NULL,%s,%s,%s,%s)"
                do_sql(sql, [olid, detail[0], detail[1], detail[2]])

    @staticmethod
    def get_open_lab_by_uid(uid):
        sql = "select * from open_lab where uid=%s"
        result = do_sql(sql, [uid])
        return result.fetchall()
