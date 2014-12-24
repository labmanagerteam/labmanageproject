# -*- coding: utf-8 -*-
__author__ = 'wlw'


def filter_result_dict_list(r_name):
    def f(result):
        r = []
        for tr in result:
            t_dict = {}
            for (name, value) in zip(r_name, tr):
                t_dict[name] = value
            r.append(t_dict)
        return r

    return f


def filter_result_tuple_list():
    def f(result):
        l = []
        for r in result:
            l.append(r)
        return l

    return f


def filter_result_tuple_tuple():
    def f(result):
        return result

    return f