#!/usr/bin/env python
#coding:utf-8
'''
csv 文件处理
'''
import csv
import codecs
headers =['ID','UserName','Password','Age','Country']
rows =[
        (1001,'郑振','zhengzhen12312'),
        (1002,'李辉','wefsdf3r234'),
        (1003,'唐龙飞','234dsfasf3'),
        (1004,'称职','asfewfwaf'),
        (1005,'鞠娟','safdwer32'),
       ]
with codecs.open('用户.csv','a+','utf-8') as fp:
    fp_csv = csv.writer(fp)
    fp_csv.writerow(headers)
    fp_csv.writerows(rows)

