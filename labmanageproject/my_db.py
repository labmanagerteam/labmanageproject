# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.db import connection, transaction
import exceptions


def join_list(a, b):
    for t in b:
        a.append(t)
    return a

def do_sql(sql, param):
    print "sql:" + sql
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
        do_sql(sql, value_list)

    return add


def get_method(tname):
    sql = "select * from " + tname + " where "

    def get(**kwargs):
        inner_sql = sql
        v_list = []
        for (key, value) in kwargs.items():
            # if key == open_lab.BEGIN_DATE_TIME:
            # inner_sql += open_lab.END_DATE_TIME + ">%s and"
            # elif key == open_lab.END_DATE_TIME:
            #     pass
            # elif key == open_lab_detail.BEGIN_TIME:
            #     pass
            # elif key == open_lab_detail.END_TIME:
            #     pass
            # else:
            inner_sql += key + "=%s and"
            v_list.append(value)
        inner_sql += " 1=1"
        print inner_sql
        result = do_sql(inner_sql, v_list)
        return result.fetchall()

    return get


def update_mothed(tname):
    sql = "update " + tname + " set "

    def update(update_dict, where_dict):
        inner_sql = sql
        value_list = []
        update_str = ""
        for (key, value) in update_dict.items():
            update_str += key + "=%s "
            value_list.append(value)
        inner_sql += update_str + " where "
        where_sql = ""
        for (key, value) in where_dict.items():
            where_sql += key + "=%s and "
            value_list.append(value)
        where_sql += " 1=1 "
        inner_sql += where_sql
        do_sql(inner_sql, value_list)

    return update


def get_department_id_by_name(dname):
    sql = "select gid from department where dname=%s"
    cursor = do_sql(sql, [dname])
    return cursor.fetchall()[0][0]


def get_card_number(uid):
    return "11223344"


def add_department(did, dname):
    sql = "insert into department(did,dname) values(%s,%s)"
    do_sql(sql, [did, dname])


class department():
    DID = 'did'
    DNAME = 'dname'



class user():
    UID = 'uid'
    UNAME = 'uname'


class lab_center():
    LCID = 'lcid'
    LCNAME = 'LCNAME'


class lab():
    LID = 'lid'
    LNAME = 'lname'
    LCID = lab_center.LCID
    LNUMBER = 'number'

    @staticmethod
    def get(**kwargs):
        return get_method('lab')(**kwargs)


class open_lab():
    OLID = 'olid'
    LCID = lab_center.LCID
    UID = 'uid'
    STATUS = 'status'
    OLNAME = 'olname'
    TYPE = 'type'
    BEGIN_DATE_TIME = 'begin_date_time'
    END_DATE_TIME = 'end_date_time'
    ACCEPT = "通过"
    REFUSE = "拒绝"
    WAIT = "未审核"

    @staticmethod
    def update(update_dict, where_dict):
        update_mothed("open_lab")(update_dict, where_dict)


class open_lab_detail:
    OLID = open_lab.OLID
    LID = lab.LID
    BEGIN_TIME = 'begin_time'
    END_TIME = 'end_time'
    OLDID = 'oldid'
    LNUMBER = lab.LNUMBER
    NAME_LIST = [OLDID, OLID, LID, BEGIN_TIME, END_TIME, LNUMBER]

    @staticmethod
    def get(**kwargs):
        return get_method('open_lab_detail')(**kwargs)

    @staticmethod
    def update(update_dict, where_dict):
        update_mothed("open_lab_detail")(update_dict, where_dict)


class user_order:
    ORDER_ID = 'order_id'
    UID = user.UID
    OLDID = open_lab_detail.OLDID
    STATE = 'state'
    NAME_LIST = [ORDER_ID, UID, OLDID, STATE]
    ACCEPT = "通过"
    REFUSE = "拒绝"
    WAIT = "未审核"

    @staticmethod
    def add(*args):
        sql = "insert into user_order(order_id,uid,oldid,state)values(NULL,%s,%s,%s)"
        do_sql(sql, args)

    @staticmethod
    def get(**kwargs):
        return get_method('user_order')(**kwargs)

    @staticmethod
    def update(update_dict, where_dict):
        update_mothed('user_order')(update_dict, where_dict)


add_user_table = add_method('user', ['uid', 'uname', 'password', 'card_number'])
add_teacher_table = add_method('teacher', ['uid', 'lcid'])
add_student_table = add_method('student', ['uid', 'did', 'grade'])
add_administer_table = add_method('administer', ['uid', 'lcid'])
add_open_lab_table = add_method('open_lab', ['olid', 'lcid', 'uid', 'begin_date_time',
                                             'end_date_time', 'status', 'olname', 'type'])

get_user_table = get_method('user')
get_student_table = get_method('student')
get_teacher_table = get_method('teacher')
get_administer_table = get_method('administer')
get_lab_center_table = get_method('lab_center')
get_department_table = get_method('department')


update_open_lab_table = update_mothed('open_lab')
LIMIT = 'limit'


class user_db():

    @staticmethod
    def add_student(uid, uname, password, card_number, grade, did):
        with transaction.atomic():
            sql = "insert into user(uid,uname,password,card_number) " \
                  "VALUES(%s,%s,%s,%s)"
            do_sql(sql, [uid, uname, password, card_number])
            sql = "insert into student(uid,did,grade) values(%s,%s,%s)"
            do_sql(sql, [uid, did, grade])

    @staticmethod
    def add_student_list(student_list):
        print "add_student_list"
        sql1 = "insert into user(uid,uname,password,card_number) " \
               "VALUES(%s,%s,%s,%s)"
        sql2 = "insert into student(uid,did,grade) values(%s,%s,%s)"
        first_student = student_list[0]
        value1 = [first_student[0], first_student[1], first_student[2], first_student[3]]
        value2 = [first_student[0], first_student[4], first_student[5]]
        for student in student_list[1:len(student_list)]:
            sql1 += ",(%s,%s,%s,%s)"
            sql2 += ",(%s,%s,%s)"
            value1 = join_list(value1, [student[0], student[1], student[2], student[3]])
            value2 = join_list(value2, [student[0], student[4], student[5]])
        do_sql(sql1, value1)
        do_sql(sql2, value2)

    @staticmethod
    def delete_student():
        pass

    @staticmethod
    def add_teacher(uid, uname, password, lcid, card_number):
        with transaction.atomic():
            sql = "insert into user(uid, uname, password, card_number)" \
                  "values(%s,%s,%s,%s)"
            do_sql(sql, [uid, uname, password, card_number])
            sql = "insert into teacher(uid, lcid)" \
                  "values(%s,%s)"
            do_sql(sql, [uid, lcid])

    @staticmethod
    def add_teacher_list(teacher_list):
        print "add_teacher_list"
        sql1 = "insert into user(uid, uname, password, card_number)" \
               "values(%s,%s,%s,%s)"
        value1 = [teacher_list[0][0], teacher_list[0][1], teacher_list[0][2], teacher_list[0][3]]
        sql2 = "insert into teacher(uid, lcid)" \
               "values(%s,%s)"
        value2 = [teacher_list[0][0], teacher_list[0][4]]
        print "wrap sql"
        for teacher in teacher_list[1:len(teacher_list)]:
            sql1 += ",(%s,%s,%s,%s)"
            sql2 += ",(%s,%s)"
            value1 = join_list(value1, [teacher[0], teacher[1], teacher[2], teacher[3]])
            value2 = join_list(value2, [teacher[0], teacher[4]])
        print "do_sql"
        do_sql(sql1, value1)
        do_sql(sql2, value2)

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
    def get_lab_center_by_lcid(lcid):
        return get_lab_center_table(**{lab_center.LCID: lcid})

    @staticmethod
    def get_all_lab_by_lcid(lcid):
        sql = "select lid,lname from lab where lcid=%s"
        result = do_sql(sql, [lcid])
        return result.fetchall()

    @staticmethod
    def get_checked_open_lab(lid, begin_time, end_time):
        sql = 'select ol.olname,  ol.begin_date_time, ol.end_date_time, ol.status, ol.type ' \
              'from open_lab ol, open_lab_detail old ' \
              'where ol.olid=old.olid and ol.status="通过" and old.begin_time<%s and old.end_time>%s and old.lid=%s'

        return do_sql(sql, [end_time, begin_time, lid]).fetchall()

    @staticmethod
    def get_all_unchecked_open_lab(begin_line_number, page_size):
        print type(begin_line_number)
        sql = 'select ol.olname, u.uname, lc.lcname, ol.type, ol.begin_date_time, ol.end_date_time, ol.olid ' \
              'from open_lab ol, user u, lab_center lc ' \
              'where ol.status="未审核" and ol.lcid=lc.lcid and ol.uid=u.uid ' \
              'limit %s,%s'
        return do_sql(sql, [begin_line_number, page_size]).fetchall()

    @staticmethod
    def get_conflict_open_lab(lid, begin_time, end_time, status):
        sql = 'select ol.olname, u.uname, lc.lcname, ol.type, ol.begin_date_time, ol.end_date_time, ol.olid ' \
              'from open_lab ol, open_lab_detail old, user u, lab_center lc ' \
              'where ol.olid=old.olid and ol.status=%s and old.begin_time<%s and old.end_time>%s and old.lid=%s ' \
              'and u.uid=ol.uid and lc.lcid=ol.lcid'
        return do_sql(sql, [status, begin_time, end_time, lid])

    @staticmethod
    def get_open_lab(**kwargs):

        inner_sql = 'select ol.olname, u.uname, lc.lcname, ol.type, ol.begin_date_time, ol.end_date_time, ol.olid ' \
                    'from open_lab ol, user u, lab_center lc ' \
                    'where '
        value_list = []
        for (key, value) in kwargs.items():
            if key == open_lab.BEGIN_DATE_TIME:
                inner_sql += "ol." + open_lab.END_DATE_TIME + ">%s and "
            elif key == open_lab.END_DATE_TIME:
                inner_sql += "ol." + open_lab.BEGIN_DATE_TIME + "<%s and "
            elif key == "limit":
                continue
            else:
                inner_sql += "ol." + key + "=%s and "
            value_list.append(value)
        inner_sql += 'ol.lcid=lc.lcid and ol.uid=u.uid '
        if LIMIT in kwargs:
            inner_sql += "limit %s,%s"
            value_list.append(kwargs[LIMIT][0])
            value_list.append(kwargs[LIMIT][1])
        return do_sql(inner_sql, value_list).fetchall()

    @staticmethod
    def get_open_lab_detail(**kwargs):
        inner_sql = 'select l.lname, old.begin_time, old.end_time, l.number, old.oldid ' \
                    'from open_lab_detail old, lab l ' \
                    'where '
        value_list = []
        for (key, value) in kwargs.items():
            if key == open_lab_detail.BEGIN_TIME:
                inner_sql += "old." + open_lab_detail.END_TIME + '>%s and '
            elif key == open_lab_detail.END_TIME:
                inner_sql += "old." + open_lab_detail.BEGIN_TIME + '<%s and '
            else:
                inner_sql += "old." + key + '=%s and '
            value_list.append(value)
        inner_sql += 'old.lid=l.lid '
        return do_sql(inner_sql, value_list).fetchall()

    @staticmethod
    def add_open_lab(olid, lcid, olname, uid, begin_date_time, end_date_time, type, detail_list):
        sql = "insert into open_lab(olid, lcid, olname, uid, begin_date_time, end_date_time, type)" \
              "values(%s,%s,%s,%s,%s,%s,%s)"
        do_sql(sql, [olid, lcid, olname, uid, begin_date_time, end_date_time, type])

        for detail in detail_list:
            sql = "insert into open_lab_detail(oldid, olid, lid, begin_time, end_time)" \
                  "values(NULL,%s,%s,%s,%s)"
            do_sql(sql, [olid, detail[0], detail[1], detail[2]])

    @staticmethod
    def get_open_lab_by_uid(uid):
        sql = "select * from open_lab where uid=%s"
        result = do_sql(sql, [uid])
        return result.fetchall()


    @staticmethod
    def get_all_checked_open_lab(line_number, page_size):
        return lab_db.get_open_lab(**{LIMIT: [int(line_number), int(page_size)], open_lab.STATUS: open_lab.ACCEPT})


    @staticmethod
    def get_open_lab_detail_by_oldid(oldid):
        return open_lab_detail.get(**{open_lab_detail.OLDID: oldid})

    @staticmethod
    def get_lab_by_lid(lid):
        return lab.get(**{lab.LID: lid})

    @staticmethod
    def add_user_order(oldid, uid):
        user_order.add(*[uid, oldid, "未审核"])


    @staticmethod
    def get_order_to_my_open_lab(uid):
        sql = "select ol.olid , old.oldid, ol.olname, uo.uid, uo.order_id," \
              "u.uname, l.lname, lc.lcname " \
              "from user_order uo, open_lab ol, open_lab_detail old, user u, lab l, lab_center lc " \
              "where ol.uid = %s and ol.olid=old.olid and old.oldid=uo.oldid " \
              "and u.uid=uo.uid and lc.lcid=ol.lcid and l.lid=old.lid " \
              "and uo.state=%s"
        return do_sql(sql, [uid, user_order.WAIT]).fetchall()
