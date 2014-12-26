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


class lab():
    BEGIN_DATE_TIME = "begin_time"
    END_DATE_TIME = "end_time"
    UID = "uid"
    LAB_ID = "lab_id"
    EXAMINE_STATUS = "examine_status"

    STATUS = {
        'accept': "通过",
        'wait': "待审核",
        'refuse': "拒绝",
    }

    def __init__(self):
        raise exceptions.Exception("这个类不应该实例化")


    @staticmethod
    def get_lab_open(my_filter, attribute_value_dict):
        """dict_list_filter should use ['uname','lab','begin_date_time','end_date_time']"""
        attribute_sql_dict = {
            lab.BEGIN_DATE_TIME: " lo.end_time>%s ",
            lab.END_DATE_TIME: " lo.begin_time<%s ",
            lab.UID: " lo.uid=%s ",
            lab.LAB_ID: " lo.lab_id=%s ",
            lab.EXAMINE_STATUS: " examine_status=%s ",
        }
        attribute_value_list = []
        sql = "select u.uname,l.lab_name,lo.begin_time,lo.end_time from lab_open lo,lab l,user u where"
        # print attribute_value_dict
        for (key, value) in attribute_value_dict.items():
            sql += attribute_sql_dict[key] + "and"
            attribute_value_list.append(value)
        sql = sql[0:len(sql) - 3]
        sql += "and lo.uid=u.uid and lo.lab_id=l.lab_id"
        print sql
        cursor = do_sql(sql, attribute_value_list)
        return my_filter(cursor.fetchall())

    @staticmethod
    def get_lab(my_filter):
        """dict_list_filter should use ['lab_id']"""
        sql = "select lab_id,lab_name from lab"
        cursor = do_sql(sql, [])
        return my_filter(cursor.fetchall())

    @staticmethod
    def add_open_lab(attribute_value_dict):
        sql = "insert into lab_open(%s) values(%s)"
        name_sql = ""
        value_sql = ""
        value_list = []
        for key, value in attribute_value_dict.items():
            name_sql += key + ","
            value_sql += "%s,"
            value_list.append(value)

        name_sql = name_sql[0:len(name_sql) - 1]
        value_sql = value_sql[0:len(value_sql) - 1]

        print sql % (name_sql, value_sql)

        do_sql(sql % (name_sql, value_sql), value_list)

