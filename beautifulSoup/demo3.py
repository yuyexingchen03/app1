#!/usr/bin/env python
#coding:utf-8

import bs4
from bs4 import BeautifulSoup
import codecs
soup =BeautifulSoup(codecs.open('index.html','r','utf-8'),'lxml')
'''
    获取节点内容
    .string
        当标签里面没有子记或者只有为一个的一个标记,就会返回文本,否则返回None
'''


'''
    .strings主要应用于tag包含多个字符串的情况下,可以循环遍历
'''

'''
    .stripped_strings 可以用于去除空白和转行返回字符串数组
'''