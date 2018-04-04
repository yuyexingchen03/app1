#!/usr/bin/env python
#coding:utf-8
import re

#将正则表达式编译成pattern对象
partten =re.compile(r'\d+')#匹配至少一个数字
#使用re.match 匹配文本,获得匹配结果,无法匹配时将返回None
'''
match 从文本开头进行匹配 匹配到立即返回 .字符开头不符合立即返回None
'''
result1 =re.match(partten,'192asdasdfa 欠我的群无 123123 12')
if result1:
    print(result1.group())
else:
    print('匹配失败1')

result2 =re.match(partten,'abc192')
if result2:
    print(result2.group())
else:
    print("匹配失败2")


'''
search 会整个扫描字符串 
    返回第一个匹配的字符串
'''
result3 = re.search(partten,'192asdasdfa 欠我的群无 123123 12')
if result3:
    print(result3.group())
else:
    print('匹配失败3')

'''
split
    会按照正则切割字符串 maxsplit可以指定切割的最大次数
'''
result4 =re.split(partten,'1大23阿萨德5地方9 的 3东风风光')
print(result4)


'''
findall
    搜索整个string,一列表的形式返回所有能匹配的字符串
'''
result5 =re.findall(partten,'1231zsdfawfq23单位爱我如发生23423')
if result5:
    print(result5)
else:
    print('匹配失败5')

'''
finditer 
    类似findall ,这里返回的是迭代器 ,更省内存,迭代器内存放的是对象
'''
result6 =re.finditer(partten,'1231zsdfawfq23单位爱我如发生23423')
for i in result6:
    print(i.group())

'''
sub
    替换
'''
p = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)')
w = 'i say, hello world!'
print()

'''
subn
    替换
'''

