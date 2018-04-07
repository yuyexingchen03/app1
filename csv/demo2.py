#!/usr/bin/env python
#coding:utf-8
'''
csv 文件处理
'''
import csv
import codecs
headers =['ID','UserName','Password','Age','Country']
rows =[
    {'ID':'2001','UserName':'汤德坤','Password':'asdsadf213213','Age':'123','Country':'China'},
    {'ID':'2002','UserName':'Nikc','Password':'asdsadf213213','Age':'123','Country':'China'},
    {'ID':'2003','UserName':'Tom','Password':'asdsadf213213','Age':'123','Country':'China'},
    {'ID':'2004','UserName':'Json','Password':'asdsadf213213','Age':'123','Country':'China'},
       ]
with codecs.open('用户.csv','a+','utf-8') as fp:
    fp_csv = csv.DictWriter(fp,fieldnames=headers)
    fp_csv.writeheader()
    fp_csv.writerows(rows)

