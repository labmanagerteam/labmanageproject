# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django import template
from labmanageproject.lab_manage import *

register = template.Library()

OPEN_LAB_TITLE_LIST = [u'开放计划名称', u'申请人', u'实验中心', u'开放计划类型', u'开放计划类型', u'计划结束时间']
OPEN_LAB_DETAIL_TITLE_LIST = [u'实验室', u'日期', u'开始时间', u'结束时间']
OPEN_LAB_CIRCLE_TITLE_LIST = [u'实验室', u'星期几', u'开始时间', u'结束时间']


def wrap_by_th(a):
    return u'<th>%s</th>' % a


def wrap_week_day(weekday):
    d = [u'星期一', u'星期二', u'星期三', u'星期四', u'星期五', u'星期六', u'星期日']
    return d[int(weekday)]


@register.simple_tag
def display_open_lab_title():
    mstr = u''
    for n in OPEN_LAB_TITLE_LIST:
        mstr += wrap_by_th(n)

    return mstr


@register.simple_tag
def display_open_lab_detail_title(mtype):
    mstr = u""
    if mtype == u"单次":
        for n in OPEN_LAB_DETAIL_TITLE_LIST:
            mstr += wrap_by_th(n)
    elif mtype == u"循环":
        for n in OPEN_LAB_CIRCLE_TITLE_LIST:
            mstr += wrap_by_th(n)
    return mstr


@register.simple_tag
def display_open_lab_body(open_lab):
    print "open_lab:%s" % open_lab
    body = u'<table>' \
           u'<tr>' \
           u'<th>开放计划名称</th>' \
           u'<td>%s</td>' \
           u'</tr>' \
           u'<tr>' \
           u'<th>申请人</th>' \
           u'<td>%s</td>' \
           u'</tr>' \
           u'<tr>' \
           u'<th>实验中心</th>' \
           u'<td>%s</td>' \
           u'</tr>' \
           u'<tr>' \
           u'<th>开放计划类型</th>' \
           u'<td>%s</td>' \
           u'</tr>' \
           u'<tr>' \
           u'<th>计划开始时间</th>' \
           u'<td>%s</td>' \
           u'</tr>' \
           u'<tr>' \
           u'<th>计划结束时间</th>' \
           u'<td>%s</td>' \
           u'</tr>' \
           u'<input type="hidden" name="olid" value="%s" />' \
           u'</table>'
    body.encode('utf-8')
    return body % (open_lab[OLNAME], open_lab[UNAME], open_lab[LCNAME], open_lab[TYPE]
                   , open_lab[BEGIN_DATE_TIME].encode('utf-8'), open_lab[END_DATE_TIME].encode('utf8'),
                   open_lab[OLID].encode('utf-8'))


def pack_detail_one_line(d):
    one_line = u'<input type="hidden" name="oldid" value="%s" /> ' \
               u'<td>%s</td>' \
               u'<td>%s</td>' \
               u'<td>%s</td>' \
               u'<td>%s</td>'
    one_line.encode('utf-8')
    return one_line % (d[OLDID], d[LNAME], d[BEGIN_TIME].strftime('%Y-%m-%d'),
                       d[BEGIN_TIME].strftime('%H:00'), d[END_TIME].strftime('%H:00'))


def pack_circle_detail_one_line(d):
    one_line = u'<input type="hidden" name="coldid" value="%s" />' \
               u'<td>%s</td>' \
               u'<td>%s</td>' \
               u'<td>%s</td>' \
               u'<td>%s</td>'
    one_line.encode('utf-8')
    return one_line % (d[circle_open_lab_detail.COLDID], d[LNAME],
                       wrap_week_day(d[circle_open_lab_detail.WEEKDAY]), d[circle_open_lab_detail.BEGIN_TIME],
                       d[circle_open_lab_detail.END_TIME])


@register.simple_tag
def display_open_one_lab_detail(detail):
    print "display_open_one_lab_detail"
    return pack_detail_one_line(detail)


@register.simple_tag
def display_circle_open_lab_detail(detail):
    print "display_circle_open_lab_detail"
    return pack_circle_detail_one_line(detail)


def get_context(context, m_str):
    print type(m_str)
    m_str = m_str.split('.')
    now = context
    print 'go down'
    for s in m_str:
        now = now[s]
    return now


def pack_detail_list(detail, mtype):
    detail_list = ""
    if mtype == u"单次":
        detail_list = u"<table>" \
                      u"<tr>" \
                      u"<th>实验室</th>" \
                      u"<th>日期</th>" \
                      u"<th>开始时间</th>" \
                      u"<th>结束时间</th>" \
                      u"</tr>"
        detail_list.encode('utf-8')
        for d in detail:
            detail_list += u'<tr>' + pack_detail_one_line(d) + u'</tr>'
        detail_list += u"</table>"
    elif mtype == u"循环":
        detail_list = u'<table>' \
                      u'<tr>' \
                      u'<th>实验室</th>' \
                      u'<th>星期几</th>' \
                      u'<th>开始时间</th>' \
                      u'<th>结束时间</th>' \
                      u'</tr>'
        detail_list.encode('utf-8')
        for d in detail:
            detail_list += u'<tr>' + pack_circle_detail_one_line(d) + u'</tr>'
        detail_list += u"</table>"
    else:
        print "no in part"
        pass
    return detail_list


class DispDetailNode(template.Node):
    def __init__(self, detail_str, mtype_str):
        self.detail_str = detail_str
        self.mtype_str = mtype_str

    def render(self, context):
        # print "context:%s" % context
        detail = get_context(context, self.detail_str)
        mtype = get_context(context, self.mtype_str)
        detail_list = pack_detail_list(detail, mtype)

        print detail_list
        return detail_list


@register.tag(name='display_open_lab_detail')
def display_open_lab_detail(parser, token):
    try:
        tag_name, detail, mtype = token.split_contents()
        print 'detail:%s' % detail
        print 'type: %s' % mtype
        #
        # raise Exception('can not in part')
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)

    return DispDetailNode(detail, mtype)


def pack_total_open_lab(body, detail):
    t_string = u'<div>' \
               u'<div>' \
               u'开放计划:'
    t_string += display_open_lab_body(body)
    t_string += u'</div>' \
                u'<div>' \
                u'具体细节:'
    t_string += pack_detail_list(detail, body[TYPE])
    t_string += u'</div>'

    print t_string

    return t_string


class DispTotalOpenLabNode(template.Node):
    def __init__(self, body_str, detail_str):
        self.body_str = body_str
        self.detail_str = detail_str

    def render(self, context):
        body = get_context(context, self.body_str)
        detail = get_context(context, self.detail_str)

        t_string = pack_total_open_lab(body, detail)

        return t_string


@register.tag(name='display_total_open_lab')
def display_total_open_lab(parser, token):
    try:
        tag_name, body, detail = token.split_contents()
        # print "disp total"
    except ValueError:
        msg = '%r tag requires two argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return DispTotalOpenLabNode(body, detail)


def wrap_by_td(a):
    return u"<td>%s</td>" % a


def wrap_by_tr(a):
    return u"<tr>%s</tr>" % a


OPEN_LAB_NAME_LIST = [OLNAME, UNAME, LCNAME, TYPE, BEGIN_DATE_TIME, END_DATE_TIME]


@register.simple_tag
def display_open_lab_in_oneline(open_lab):
    one_line = u'<input type="hidden" name="olid" value="%s" />' % open_lab[OLID]
    for n in OPEN_LAB_NAME_LIST:
        one_line += wrap_by_td(open_lab[n])
    # print u"display_open_lab_in_oneline:%s" % one_line
    return one_line


def display_title(titls_list):
    s = u""
    for t in titls_list:
        s += wrap_by_th(t)
    return s


ORDER_CHECK_TITLE_LIST = [u'开放计划名称', u'实验中心', u'实验室', u'申请人学号', u'申请人姓名']


@register.simple_tag
def display_order_title():
    return display_title(ORDER_CHECK_TITLE_LIST)


def pack_order_one_line(body, extra_body):
    if body[TYPE] == open_lab.ONE_TIME:
        one_line = u'<td>' \
                   u'<input type="hidden" name="order_id" value="%s"/>' \
                   u'<input type="hidden" name="uid" value="%s"/>' \
                   u'<input type="hidden" name="type" value="one_time" /> ' \
                   u'%s' \
                   u'</td>' \
                   u'<td>%s</td>' \
                   u'<td>%s</td>' \
                   u'<td>%s</td>' \
                   u'<td>%s</td>' \
                   u'%s'

        return one_line % (body[ORDER_ID], body[UID], body[OLNAME], body[LCNAME]
                           , body[LNAME], body[UID], body[UNAME], extra_body)
    elif body[TYPE] == open_lab.CIRCLE:
        one_line = u'<td>' \
                   u'<input type="hidden" name="corder_id" value="%s"/>' \
                   u'<input type="hidden" name="uid" value="%s"/>' \
                   u'<input type="hidden" name="type" value="circle" /> ' \
                   u'%s' \
                   u'</td>' \
                   u'<td>%s</td>' \
                   u'<td>%s</td>' \
                   u'<td>%s</td>' \
                   u'<td>%s</td>' \
                   u'%s'
        return one_line % (body[circle_order.CORDER_ID], body[UID], body[OLNAME], body[LCNAME]
                           , body[LNAME], body[UID], body[UNAME], extra_body)
    else:
        return u""


def pack_order_list(body, extra_body):
    s = u''
    for b in body:
        s += wrap_by_tr(pack_order_one_line(b, extra_body))

    return s


class DispOrderBodyNode(template.Node):
    def __init__(self, body, extra_body):
        self.body = body
        self.extra_body = extra_body

    def render(self, context):
        body = get_context(context, self.body)
        extra_body = get_context(context, self.extra_body)
        # extra_body = self.extra_body

        return pack_order_list(body, extra_body)


@register.tag(name='display_order_body')
def display_open_lab_detail(parser, token):
    try:
        tag_name, body, extra_body = token.split_contents()
        print '%s' % tag_name
        print 'detail:%s' % body
        print 'type: %s' % extra_body
        #
        # raise Exception('can not in part')
    except ValueError:
        msg = '%r tag requires two arguments' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)

    return DispOrderBodyNode(body, extra_body)


@register.simple_tag
def display_order_body_state(order_body):
    s = u''
    for o in order_body:
        extra = o[STATE]
        if extra == u"通过":
            extra += u" 座位号是%s" % o[user_order.SEAT_ID]
        extra = wrap_by_td(extra)
        s += wrap_by_tr(pack_order_one_line(o, extra))

    return s
