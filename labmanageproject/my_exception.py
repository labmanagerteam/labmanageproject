# -*- coding: utf-8 -*-
__author__ = 'wlw'
from exceptions import Exception


class NotPostException(Exception):
    pass


class NotFillFieldError(Exception):
    pass


class FormInValidError(Exception):
    pass