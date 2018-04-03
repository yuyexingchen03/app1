#!/usr/bin/env python
#coding=utf-8
'''
get请求演示
'''
from urllib import request
#一步到位
re =request.urlopen('http://www.zhihu.com')
html =re.read()
print(html)
re.close()
#分成请求和响应方式写
req = request.Request("http://www.baidu.com")#请求
res = request.urlopen(req)#响应
html =res.read()
print(html)


