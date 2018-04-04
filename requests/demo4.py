#!/usr/bin/env python
#coding:utf-8
import requests
import chardet
from urllib.parse import urljoin

'''
自动处理cookie访问方式

'''
logininUrl = 'http://dzsb.kyd2002.com:8080/userLogin.do'
postdata = {'roleId':'0','userName':'admin','password':'dzsb07012015'}
s =requests.session()

r = s.post(logininUrl,data=postdata)
print(r.json()['path'])
r = s.get(urljoin(logininUrl,r.json()['path']))
print(r.text)

'''
重定向与历史信息
    allow_redirects 可以设置社否可以重定向
    s.history可以查看重定向的历史记录
'''
r = requests.get('http://github.com',allow_redirects=False)
print(r.url)
print(r.status_code)
print(r.history)

'''
超时设置
    timeout 时间单位为s
'''
r =requests.get('http://github.com',timeout = 2)
print(r.status_code)


'''
代理设置

'''
proxies = {
    'http':'http://0.10.1.10:3128',
    'https':'http://0.10.1.10:1080'
}

r = requests.get("http://example.org",proxies=proxies)
print("代理:",r.status_code)




