from django.test import TestCase

from web.tools.md5 import curlmd5

src = '123456'
print('原始值：'+src)
print('计算结果：' + curlmd5(src))

src = '你好'
print('原始值：'+src)
print('计算结果：' + curlmd5(src))