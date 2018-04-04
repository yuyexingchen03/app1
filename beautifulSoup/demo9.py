#!/usr/bin/env python
#coding:utf-8
'''
    搜索文档树
       另外
        find
        find_parents
        find_parent
        find_next_siblings
        find_next_sibling
        find_previous_siblings
        find_previous_sibling
        ....等类似
'''
import bs4
from bs4 import BeautifulSoup
import codecs
import re
soup =BeautifulSoup(codecs.open('index.html','r','utf-8'),'lxml')
