# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.db import connection, transaction


def filter_result(result, r_name):
    r = []
    for tr in result:
        t_dict = {}
        for (name, value) in zip(r_name, tr):
            t_dict[name] = value
        r.append(t_dict)
    return r


def filter_result_tuple_list(result):
    l = []
    for r in result:
        l.append(r)
    return l


def do_sql(sql, param):
    cursor = connection.cursor()
    cursor.execute(sql, param)
    return cursor


def get_user(uid, password):
    print uid, password
    sql = "select uname from user where uid=%s and password = %s"
    cursor = do_sql(sql, [uid, password])
    result = cursor.fetchall()
    print result
    return filter_result(result, ['uname'])


def get_identity(uid):
    sql = "select i.gname from user_identity ui,identity i where ui.uid=%s and i.gid=ui.gid"
    cursor = do_sql(sql, [uid])
    return filter_result(cursor.fetchall(), ['identity'])


def get_identity_id(uid):
    sql = "select ui.gid from user_identity ui where ui.uid=%s"
    cursor = do_sql(sql, [uid])
    return filter_result(cursor.fetchall(), ['gid'])


def get_user_perm(uid):
    sql = "select p.pname,p.url from user_perm up,perm p where up.uid=%sand p.pid=up.pid"
    cursor = do_sql(sql, [uid])
    return filter_result(cursor.fetchall(), ['pname', 'url'])


def get_uer_identity_perm(uid):
    sql = "select p.pname,p.url from identity_perm ip,user_identity ui,perm p where ui.uid=%s and ip.gid=ui.gid and p.pid=ip.pid"
    cursor = do_sql(sql, [uid])
    return filter_result(cursor.fetchall(), ['pname', 'url'])


def get_lab():
    sql = "select lab_id,lab_name from lab"
    cursor = do_sql(sql, [])
    return filter_result_tuple_list(cursor.fetchall())

