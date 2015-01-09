# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django import forms


class my_date_field(forms.DateField):
    class my_data_input(forms.DateInput):
        format_key = 'DATE_INPUT_FORMATS'
        input_type = 'date'

    widget = my_data_input()


class my_time_field(forms.ChoiceField):
    choices = [(i, i) for i in xrange(8, 23)]
