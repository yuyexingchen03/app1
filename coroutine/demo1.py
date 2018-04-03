#!/usr/bin/env python
#coding=utf-8
'''
由于monkey在IO操作时自动启动协程
所以改写了python部分标准库,例如Io,socket等
所以我们在之前需要执行monkey.patch_all()改写库文件
'''
from gevent import monkey;monkey.patch_all()
import gevent
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
#协程访问方式
def coroutine_demo():
    startTime = time.time()
    urls = ['https://github.com', 'https://www.python.org/', 'https://www.baidu.com']
    # spawn 方法用来形成协程  joinall方法添加这些协程任务,并且启动永兴
    greeenlets = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(greeenlets)
    endTime = time.time()
    print('use time %d %s' % (endTime - startTime))
#普通访问的方式
def common_demo():
    startTime = time.time()
    urls = ['https://github.com', 'https://www.python.org/', 'https://www.baidu.com']
    for url in urls:
        run_task(url)
    endTime = time.time()
    print('use time %d %s' % (endTime - startTime))

if __name__ == '__main__':
    #协程方式访问
    coroutine_demo()
    #普通方式访问
    common_demo()