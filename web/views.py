from django.shortcuts import render
from web.models import User
from time import time
from web.tools.md5 import curlmd5
from web.tools.json_tool import dict_to_json, class_to_dict
from django.http import HttpResponse

"""
使用手机号以及密码来登录，登陆完成以后给用户返回了一个token
"""
def login(request):
    phone_num = request.GET.get('phone_num')
    password = request.GET.get('password')
    users = User.objects.filter(phone_num__exact=phone_num, password__exact=password)
    if len(users) > 0:
        token = curlmd5(str(time()) + phone_num)
        result = {'result': 1, 'token': token}
        user = users[0]
        user.token = token
        user.save()
    else:
        result = {'result': 0}
    return HttpResponse(dict_to_json(result))

"""
验证token
"""
def check_token(req):
    phone_num = req.GET.get('phone_num')
    token = req.GET.get('token')
    users = User.objects.filter(phone_num__exact=phone_num, token__exact=token)
    if len(users) > 0:
        result = {'result': 1}
    else:
        result = {'result': 0}
    return HttpResponse(dict_to_json(result))

"""
得到用户的个人信息
"""
def get_user_info(req):
    phone_num = req.GET.get('phone_num')
    token = req.GET.get('token')
    users = User.objects.filter(token__exact=token, phone_num__exact=phone_num)
    if len(users) > 0:
        user = users[0]
        user.register_time = str(user.register_time)
        user_dict = class_to_dict(user)
        user_dict['result'] = 1
        user_dict.pop('_state')
        user_dict.pop('register_time')
        user_dict.pop('password')
    else:
        user_dict = {'result': 0}
    return HttpResponse(dict_to_json(user_dict))

