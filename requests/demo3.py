#!/usr/bin/env python
#coding:utf-8
import requests
import chardet
from urllib.parse import urljoin
'''
请求头的设置
'''
user_agent ='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers ={'User-Agent':user_agent}
r =requests.get("https://www.baidu.com",headers =headers)
print(r.text)

'''
响应吗code和响应投headers处理
'''
print(r.status_code)
if r.status_code == 200:
    print(r.headers)#响应头
    print(r.headers.get("content-type"))#获取具体某个响应投
else:
    r.raise_for_status()
#r.raise_for_status会抛出异常


'''
cookie处理

'''
#遍历cookie
for cookie in r.cookies.keys():
    print(cookie,"----------->>>",r.cookies.get(cookie))

'''
自定义cookie访问

'''
user_agent ='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers ={'User-Agent':user_agent}
cookies = dict(name='qiye',age='10')
r = requests.get('https://www.baidu.com',headers=headers,cookies =cookies)
print(r.text)

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




