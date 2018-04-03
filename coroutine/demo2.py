#!/usr/bin/env python
#coding=utf-8
'''
由于monkey在IO操作时自动启动协程
所以改写了python部分标准库,例如Io,socket等
所以我们在之前需要执行monkey.patch_all()改写库文件

协程池实现
'''
from gevent import monkey;monkey.patch_all()
from gevent import pool
from urllib import request
import  time
#协程执行的任务
def run_task(url):
    print('Visit --> %s'%url)
    try:
        re = request.urlopen(url)
        data = re.read()
        print('%d bytes received from %s .'%(len(data),url))
    except BaseException as e:
        print(e)
    return 'url:%s ---> finisk'%url

if __name__ == '__main__':
    #协程池方式
    pool =pool.Pool(2)
    urls= ['https://github.com', 'https://www.python.org/', 'https://www.baidu.com']
    results = pool.map(run_task,urls)
    print(results)