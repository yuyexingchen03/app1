#!/usr/bin/env python
#coding:utf-8

import bs4
from bs4 import BeautifulSoup
import codecs
'''
    获取文档注释内容
        注释属于特殊的NavigableString
'''

soup =BeautifulSoup("<b><!--Hey, buddy. Want to buy a used parser?--></b>",'lxml')
if type(soup.b.string) ==bs4.Comment:
    print(soup.b.string)


'''
    遍历文档树
        子节点.contents
        返回一个数组
        只返回直接子节点
'''
soup =BeautifulSoup(codecs.open('index.html','r','utf-8'),'lxml')
print(soup.head.contents)
print(len(soup.head.contents))

'''
    返回一个可以迭代的迭代器
        .childrean
        只返回直接子节点
'''
for child in soup.head.children:
    print(child)

'''
    返回子孙后代节点
        .descendants
'''
for child in soup.head.descendants:
    print("---->",child)