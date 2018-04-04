#!/usr/bin/env python
#coding:utf-8
'''
    搜索文档树
       limit 分页
       recursive 是否搜索包括子孙节点
'''
import bs4
from bs4 import BeautifulSoup
import codecs
import re
soup =BeautifulSoup(codecs.open('index.html','r','utf-8'),'lxml')
'''
    find_all( name , attrs , recursive , string , **kwargs )
        limit 分页
        recursive 是否只搜索直接子节点
'''

print('------------------------>>>>>>kwargs:字符串匹配<<<<------------------------------------')
for t in soup.find_all(class_=True,limit=2):
    print(t.name)


'''
    recursive
    是否搜索包括子孙节点
        False:只搜索直接子节点
        True:包含子孙节点
'''
print('------------------------>>>>>>recursive:是否搜索包括子孙节点<<<<------------------------------------')
print(soup.find_all('title'))
print(soup.find_all('title',recursive=False))