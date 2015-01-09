# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django import forms
from django.forms.formsets import formset_factory
from django.forms.formsets import BaseFormSet
from django.db import transaction
import django.utils.timezone as timezone

from labmanageproject.my_db import lab_db
from labmanageproject.my_filter import filter_result_dict_list, filter_result_tuple_list
from labmanageproject.my_exception import FormInValidError
from labmanageproject.my_field import my_date_field, my_time_field

UID = 'uid'
LCID = 'lcid'
LCNAME = 'lcname'
LID = 'lid'
LNAME = 'lname'
OLNAME = 'olname'
DATE = 'date'
BEGIN_TIME = 'begin_time'
END_TIME = 'end_time'
BEGIN_DATE_TIME = 'begin_date_time'
END_DATE_TIME = 'end_date_time'

def get_all_lab_center():
    m_filter = filter_result_dict_list([LCID, LCNAME])
    return m_filter(lab_db.get_all_lab_center())


def get_all_lab_by_lcid(lcid):
    m_filter = filter_result_dict_list([LID, LNAME])
    return m_filter(lab_db.get_all_lab_by_lcid(lcid))


def check_open_lab():
    with transaction.atomic():
        pass


def to_local_time(year, month, day, hour=0, minute=0, second=0):
    return timezone.make_aware(timezone.datetime(year, month, day, hour, minute, second),
                               timezone.get_current_timezone())


def detail_form_factory(lcid):
    class detail_form(forms.Form):
        lid = forms.ChoiceField(choices=filter_result_tuple_list()(lab_db.get_all_lab_by_lcid(lcid)))
        date = my_date_field()
        begin_time = my_time_field()
        end_time = my_time_field()

        def clean(self):
            clean_date = super(detail_form, self).clean()
            in_scope = lambda x: 8 <= x <= 22

            if not in_scope(int(clean_date[BEGIN_TIME])):
                raise forms.ValidationError("error")

            if not in_scope(int(clean_date[END_TIME])):
                raise forms.ValidationError("error")

    return detail_form


def open_lab_form_factory(init, **kwargs):
    class i_form(forms.Form):
        olname = forms.CharField(max_length=60)
        lcid = forms.ChoiceField(choices=filter_result_tuple_list()(lab_db.get_all_lab_center()))
        uid = forms.CharField(widget=forms.HiddenInput)

    if init:
        return [i_form(initial={UID: kwargs[UID]}), []]

    if LCID not in kwargs:
        kwargs[LCID] = '1'
    inner_form = i_form(kwargs)

    class open_lab_base_form(BaseFormSet):
        pass
        # def clean(self):
        # def combine_time(date, m_time):
        #         import time
        #         date_format = "%Y %m %d"
        #         d_time = time.strptime(date_format, date)
        #         return to_local_time(d_time.tm_year, d_time.tm_mon, d_time.tm_mday, m_time)
        #
        #     def check_no_time_join(form_list):
        #         def is_join(begin_a, end_a, begin_b, end_b):
        #             if begin_a < end_b and end_a > begin_b:
        #                 return True
        #             else:
        #                 return False
        #
        #         detail_list = form_list
        #
        #         for index1 in xrange(len(detail_list)):
        #             for index2 in xrange(index1+1, len(detail_list)):
        #                 if detail_list[index1][LID] == detail_list[index2][LID] and \
        #                         is_join(detail_list[index1][BEGIN_TIME], detail_list[index1][END_TIME],
        #                                 detail_list[BEGIN_TIME], detail_list[END_TIME]):
        #                     raise forms.ValidationError("第" + index1 + "个和第" + index2 + "个时间冲突")
        #
        #     if any(self.errors):
        #         return
        #
        #     if not inner_form.is_valid():
        #         return
        #
        #     form_list = []
        #
        #     for form in self.forms:
        #         c_data = form.cleaned_data
        #
        #         one_form = dict(lid=c_data[LID], begin_time=combine_time(c_data[DATE], c_data[BEGIN_TIME]),
        #                         end_time=combine_time(c_data[DATE], c_data[END_TIME]))
        #
        #         form_list.append(one_form)
        #
        #     check_no_time_join(form_list)
        #
        #     uid = kwargs[UID]
        #     time_format = '%Y %m %d %H %M %S'
        #     olid = uid + timezone.now().strptime(time_format)
        #     with transaction.atomic():
        #         pass

    open_lab_form = formset_factory(detail_form_factory(kwargs[LCID]), open_lab_base_form)
    return [inner_form, open_lab_form(kwargs)]


def check_open_lab(*args):
    error = [{'result': 'e'}]
    for a in args:
        if not a:
            return error

    olname = args[0]
    uid = args[1]
    lcid = args[2]
    lid = args[3]
    begin_time = args[4]
    end_time = args[5]

    if not lab_db.get_lab_center_by_lcid(lcid):
        print 'no that lcid'
        return error

    if len(lid) != len(begin_time) or len(lid) != len(end_time):
        print 'no the same length'
        return error

    s_lid = [a for (a, b) in lab_db.get_all_lab_by_lcid(lcid)]
    print s_lid
    for l in lid:
        if l not in s_lid:
            print 'no that lid'
            return error

    import datetime

    for i in xrange(len(begin_time)):
        try:
            begin_time[i] = timezone.make_aware(datetime.datetime.strptime(begin_time[i], '%Y-%m-%d %H'),
                                                timezone.get_current_timezone())
            end_time[i] = timezone.make_aware(datetime.datetime.strptime(end_time[i], '%Y-%m-%d %H'),
                                              timezone.get_current_timezone())
        except ValueError:
            print 'join error'
            return error

    index = 0
    join_list = []
    with transaction.atomic():
        for (l, b, e) in zip(lid, begin_time, end_time):
            if lab_db.get_checked_open_lab(l, b, e):
                join_list.append({'result': index})
            index += 1
        if join_list:
            return join_list
        else:
            begin_date_time = begin_time[0]
            for b in begin_time:
                if begin_date_time > b:
                    begin_date_time = b

            end_date_time = end_time[0]
            for e in end_time:
                if e > end_date_time:
                    end_date_time = e
            olid = uid + timezone.now().strftime('%Y %m %d %H %M %S')
            detail_list = [[l, b, e] for (l, b, e) in zip(lid, begin_time, end_time)]
            lab_db.add_open_lab(olid, lcid, olname, uid, begin_date_time, end_date_time, "单次", detail_list)
            return [{'result': 's'}]
