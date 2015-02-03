# -*- coding: utf-8 -*-
__author__ = 'wlw'

from django.shortcuts import render
from django.http import HttpResponseRedirect

from labmanageproject.user_manage import *
from labmanageproject.my_decorator import *
from labmanageproject.error_code import *


def get_post(request, name_list):
    value_list = []
    for name in name_list:
        value_list.append(request.POST[name])
    return value_list


def create_json_return(d):
    return HttpResponse(json.dumps(d))


def login(request):
    login_error = False
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uname = check_password(cd['uid'], cd['password'])
            # print uname
            if uname:
                perm_list = get_perm_list(cd['uid'])
                my_user = {
                    'perm_list': perm_list,
                    'uname': uname,
                    'uid': cd['uid']
                }
                request.session['my_user'] = my_user
                return render(request, 'home.html', locals())
            else:
                login_error = True
    else:
        form = login_form()
    # return render_to_response('login.html', locals(), context_instance=RequestContext(request, c))
    return render(request, 'login.html', locals())


def logout(request):
    del request.session['my_user']
    return HttpResponseRedirect('/')


def add_user_view(request):
    add_list = [
        {
            'val': '0',
            'name': 'student'
        },
        {
            'val': '1',
            'name': 'teacher'
        }
    ]
    return render(request, "add_user.html", locals())


student_distribute_list = ['uid', 'uname', 'card_number', 'grade', 'did']


@check_post_form(student_distribute_list)
def add_one_student_view(request):
    value_list = get_post(request, student_distribute_list)
    error_code = add_one_student_action(*value_list)
    if error_code:
        error_message = generate_error_message(error_code)
        return create_json_return({'result': 'error', 'msg': error_message})
    else:
        return create_json_return({'result': 'success'})


def add_student_list_view(request):
    pass


teacher_distribute_list = ['uid', 'uname', 'password', 'lcid', 'card_number']


@check_post_form(teacher_distribute_list)
def add_one_teacher_view(request):
    value_list = get_post(request, teacher_distribute_list)
    error_code = add_one_teacher_action(*value_list)
    if error_code:
        error_message = generate_error_message(error_code)
        return create_json_return({'result': 'error', 'msg': error_message})
    else:
        return create_json_return({'result': 'success'})


def add_teacher_list_view(request):
    pass