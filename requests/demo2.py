#!/usr/bin/env python
#coding:utf-8
import requests
import chardet
'''
get 请求
    带参数
'''
getdata ={'keywords':'blog:qiye','pageindex':'1'}
r =requests.get("http://zzk.cnblogs.com/s/blogpost" , params=getdata,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
print(r.url)
print(r.text)#r.content 打印的是二进制的数据 r.text()是编码以后返回数据


'''
响应和编码
    r.content 反悔的是字节的形式
    r.text 返回的是编码以后的格式
    r.encoding 返回的是猜测网页的编码格式 我们也可以手动设置 也可以导入chardet库区猜测
'''
r= requests.get("https://www.baidu.com")
print(r.content)
print(r.text)
print(r.encoding)
print(chardet.detect(r.content))

'''
读取流的流模式
'''
r = requests.get("https://www.baidu.com",stream=True)
print(r.raw.read(10))
