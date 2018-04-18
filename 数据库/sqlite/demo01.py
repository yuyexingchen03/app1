#!/usr/bin/env python
#coding:UTF-8
# @Time     : 2018/4/18 11:07
# @Author   : zhengzhen

import  sqlite3


# 建表
con =sqlite3.connect('e:/test.db')
cu = con.cursor()
try:
    cu.execute("create table student (id integer primary key,name varchar(20) ,age integer)")
except Exception as e:
    print("操作失败1")
finally:
    cu.close()
    con.close()

# 插入数据
con =sqlite3.connect('e:/test.db')
cu = con.cursor()
try:
    cu.execute("insert into student(name,age) values(?,?)",('郑震',20))
    con.commit()
except Exception as e:
    print("操作失败2")
    con.rollback()
finally:
    cu.close()
    con.close()


# d多条插入数据
con =sqlite3.connect('e:/test.db')
cu = con.cursor()
try:
    cu.executemany("insert into student(name,age) values(?,?)",[('郑震',20),('李辉',25),('陈峙',26)])
    con.commit()
except Exception as e:
    print("操作失败3")
    con.rollback()
finally:
    cu.close()
    con.close()

# 查询数据
con =sqlite3.connect('e:/test.db')
cu = con.cursor()
cu.execute('select * from student')
for r in cu.fetchall():
    print(r)
# 修改和删除数据







