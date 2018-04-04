#!/usr/bin/env python
#coding:utf-8

import bs4
from bs4 import BeautifulSoup
import codecs
soup =BeautifulSoup(codecs.open('index.html','r','utf-8'),'lxml')
'''
    获取下一个兄弟节点
        .next_sibling
'''

'''
    获取上一个兄弟节点
        .previous_sibling
'''

'''
    .next_elements
    后一个节点:不分父子节点,区别于next_sibling
'''

'''
    .previous_elements
    前一个节点:不分父子节点,区别于previous_sibling
'''