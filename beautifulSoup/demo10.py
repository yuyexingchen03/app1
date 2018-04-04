#!/usr/bin/env python
#coding:utf-8
'''
    搜索文档树
       css选择器
       select方法
'''
import bs4
from bs4 import BeautifulSoup
import codecs
import re
soup =BeautifulSoup(codecs.open('index.html','r','utf-8'),'lxml')
for l in soup.select("head > title"):
    print(l)

'''
    可以参考jquery的css选择器
'''