# -*- coding: utf-8 -*-
__author__ = 'wlw'
from exceptions import Exception


class NotPostException(Exception):
    pass


class NotFillFieldError(Exception):
    pass


class FormInValidError(Exception):
    pass


class MyBaseException(Exception):
    def __init__(self, error_code):
        super(MyBaseException, self).__init__()
        self.error_code = error_code


class MyListException(MyBaseException):
    def __init__(self, error_code, num):
        super(MyListException, self).__init__(error_code)
        self.num = num