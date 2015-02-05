# -*- coding: utf-8 -*-
__author__ = 'wlw'

HAVE_USR = 1
NO_THAT_DEPARTMENT = 2
NO_THAT_LAB_CENTER = 3
HAVE_EMPTY = 4
LEFT_DISTRIBUTE = 5


def generate_error_message(error_code):
    d = {
        HAVE_USR: '该用户已存在',
        NO_THAT_DEPARTMENT: '不存在这个院系代码',
        NO_THAT_LAB_CENTER: '不存在这个实验中心代码',
        HAVE_EMPTY: '存在空值',
        LEFT_DISTRIBUTE: '缺少某个属性值'
    }

    return d[error_code]