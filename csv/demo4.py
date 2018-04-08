#!/usr/bin/env python
#coding:utf-8
'''
csv 文件处理
    命名元组方式读取
'''
import csv
import codecs
import collections
with codecs.open('用户.csv','r','utf-8') as fp:
    fp_csv = csv.reader(fp)
    headers = next(fp_csv)
    Row = collections.namedtuple('Row',headers)
    print(headers)
    for r in fp_csv:
        row = Row(*r)
        print(row)

