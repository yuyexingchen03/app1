#!/usr/bin/env python
#coding:utf-8
import requests
'''
get 请求
    无参数
'''
r =requests.get("http://www.baidu.com")
print(r.content)#r.content 打印的是二进制的数据 r.text()是编码以后返回数据

'''
post 请求
 无参数
'''

r =requests.post("http://www.baidu.com")

'''
delete 请求
    无参数
'''
r=requests.delete("http://www.xxxxx.com/delete")

'''
head 请求
    无参数
'''
r= requests.head("http://www.xxxxx.com/get")

'''
options 请求
    无参数
'''
r= requests.options("http://www.xxxxx.com/get")

