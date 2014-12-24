# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.db import connection, transaction


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


def get_lab(my_filter):
    """dict_list_filter should use ['lab_id']"""
    sql = "select lab_id,lab_name from lab"
    cursor = do_sql(sql, [])
    return my_filter(cursor.fetchall())


def get_lab_open_insert_time(my_filter, begin_date_time, end_date_time):
    """dict_list_filter should use ['uname','lab','begin_date_time','end_date_time']"""
    sql = "select u.uname,l.lab_name,lo.begin_time,lo.end_time from lab_open lo,lab l,user u where lo.begin_time<%s and lo.end_time>%s and lo.uid=u.uid and lo.lab_id=l.lab_id"
    cursor = do_sql(sql, [begin_date_time, end_date_time])
    return my_filter(cursor.fetchall)