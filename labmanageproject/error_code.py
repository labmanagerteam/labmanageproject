# -*- coding: utf-8 -*-
__author__ = 'wlw'

HAVE_USR = 1
NO_THAT_DEPARTMENT = 2
NO_THAT_LAB_CENTER = 3
HAVE_EMPTY = 4
LEFT_DISTRIBUTE = 5
HAVE_LAB_CENTER = 6
HAVE_LAB = 7
HAVE_DEPARTMENT = 8
NO_USER = 9
NO_LID = 10


def generate_error_message(error_code, num='false'):
    d = {
        HAVE_USR: '1该用户已存在',
        NO_THAT_DEPARTMENT: '2不存在这个院系代码',
        NO_THAT_LAB_CENTER: '3不存在这个实验中心代码',
        HAVE_EMPTY: '4存在空值',
        LEFT_DISTRIBUTE: '5缺少某个属性值',
        HAVE_LAB_CENTER: '6该实验中心以存在',
        HAVE_LAB: '7该实验室以存在',
        HAVE_DEPARTMENT: '8该院系已存在',
        NO_USER: '9该用户不存在',
        NO_LID: '10不存在这个实验室',
    }

    if num == 'false':
        return d[error_code]
    else:
        return "第%d行:%s" % (num, d[error_code])
