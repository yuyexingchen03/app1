#!/usr/bin/env python
#coding:utf-8
'''
csv 文件处理
    读取
'''
import csv
import codecs
with codecs.open('用户.csv','r','utf-8') as fp:
    fp_csv = csv.reader(fp)
    headers = next(fp_csv)
    print(headers)
    for row in fp_csv:
        print(row)

