#!/usr/bin/env python
#coding:UTF-8
# @Time     : 2018/4/18 11:49
# @Author   : zhengzhen

import mysql.connector

con = mysql.connector.connect(host='localhost',user='root',password='root',database='test',charset='utf8')
cur = con.cursor()

# 建表
# cur.execute('create table person(id int not null auto_increment primary key,name varchar(20), age int )')

# 插入数据
cur.execute('insert into person(name,age) values(%s,%s)',['郑震',20])
print(str(cur.rowcount))

con.commit()





