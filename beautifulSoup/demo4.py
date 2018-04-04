#!/usr/bin/env python
#coding:utf-8

import bs4
from bs4 import BeautifulSoup
import codecs
soup =BeautifulSoup(codecs.open('index.html','r','utf-8'),'lxml')
'''
    获取父节点   
        .parent
'''


'''
    获取父辈节点
        .parents 可以获取到根节点的所有祖宗节点
'''


