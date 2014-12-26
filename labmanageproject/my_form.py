# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django import forms


class my_date_field(forms.DateField):
    class my_data_input(forms.DateInput):
        format_key = 'DATE_INPUT_FORMATS'
        input_type = 'date'

    widget = my_data_input()


class my_base_form(forms.Form):
    def __init__(self, check, my_error_message, *args, **kwargs):
        super(my_base_form, self).__init__(*args, **kwargs)
        self.check = check
        self.my_error_message = my_error_message

    def clean(self):
        clean_data = super(my_base_form, self).clean()
        # print clean_data
        if not self.check(clean_data):
            raise forms.ValidationError(self.my_error_message)
        else:
            return clean_data


# def test_check(a):
# print a
#     return False
#
#
# class test_form(my_base_form):
#     def __init__(self, *args, **kwargs):
#         super(test_form, self).__init__(test_check, "test error", *args, **kwargs)
#     test = forms.CharField()






