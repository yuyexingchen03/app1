#!/usr/bin/env python
#coding:utf-8
'''
    搜索文档树
        kwargs搜索 属性搜索
        attrs搜索 特殊属性
        text搜索 文档内容搜索
'''
import bs4
from bs4 import BeautifulSoup
import codecs
import re
soup =BeautifulSoup(codecs.open('index.html','r','utf-8'),'lxml')
'''
    find_all( name , attrs , recursive , string , **kwargs )
        kwargs:属性搜索 类似 id ='xxx'  可以传入字符串,正则,函数,True,列表
'''

'''
    attrs:属性搜索 kwargs 搜索
'''

'''
    kwargs:字符串匹配
'''
print('------------------------>>>>>>kwargs:字符串匹配<<<<------------------------------------')
for t in soup.find_all(class_='last'):
    print(t.name)

'''
    kwargs:True匹配
'''
print('------------------------>>>>>>kwargs:True匹配<<<<------------------------------------')
for t in soup.find_all(class_=True):
    print(t.name)

'''
    kwargs:多个属性匹配
'''
print('------------------------>>>>>>kwargs:多个属性匹配<<<<------------------------------------')
for t in soup.find_all(class_=True,id='cnblogs_post_body'):
    print(t.name)

'''
    attrs:特殊属性匹配
        h5中的data-xxx特殊属性不可以做为kwargs搜索,可以用attrs包裹
'''
print('------------------------>>>>>>attrs:特殊属性匹配<<<<------------------------------------')
for t in soup.find_all(attrs={"data-foo":'value'}):
    print(t.name)

'''
    text:文档内容搜索
'''
print('------------------------>>>>>>text:文档内容搜索<<<<------------------------------------')
for t in soup.find_all(text=re.compile('Python')):
    print(t.string)