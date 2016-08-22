from django.shortcuts import render
from web.models import User
from time import time
from web.tools.md5 import curlmd5
from web.tools.json_tool import dict_to_json
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


