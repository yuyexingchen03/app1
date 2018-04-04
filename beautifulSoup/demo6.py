#!/usr/bin/env python
#coding:utf-8
'''
    搜索文档树
        name搜索
'''
import bs4
from bs4 import BeautifulSoup
import codecs
import re
soup =BeautifulSoup(codecs.open('index.html','r','utf-8'),'lxml')
'''
    find_all( name , attrs , recursive , string , **kwargs )
        name:标签名  可以传入字符串,正则,函数,True,列表
'''

'''
    name:字符串
'''
print('------------------------>>>>>>name:字符串匹配<<<<------------------------------------')
for t in soup.find_all('tr'):
    print(t.name)

'''
    name:正则表达式
'''
print('------------------------>>>>>>name:正则匹配<<<<------------------------------------')
for t in soup.find_all(re.compile(r"^t")):
    if t.string:
        print("%s ---->>>%s" % (t.name,t.string ))
    else:
        print("%s ---->>>%s" % (t.name,t.contents))

'''
    name:列表参数
'''
print('------------------------>>>>>>name:列表参数<<<<------------------------------------')
for t in soup.find_all(['td','th']):
    if t.string:
        print("%s ---->>>%s" % (t.name,t.string ))
    else:
        print("%s ---->>>%s" % (t.name,t.contents))

'''
    name:True参数  会返回所有tag,但是不会返回字符串节点
'''
print('------------------------>>>>>>name:True参数<<<<------------------------------------')
for t in soup.find_all(True):
    print(" ---->>>%s" % (t.name))

'''
    name:函数参数
'''
print('------------------------>>>>>>name:函数参数<<<<------------------------------------')
def hassClassId(tag):
    return tag.has_attr('class') and tag.has_attr('id')
for t in soup.find_all(hassClassId):
    print(" ---->>>%s" % (t.name))