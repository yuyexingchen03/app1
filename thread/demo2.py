#!/usr/bin/env python
#codiing=utf-8

import random
import time,threading
'''
线程从threading.Thread继承创建线程
,重写__init__和run()方法
'''
class MyThread(threading.Thread):
    def __init__(self,name,urls):
        threading.Thread.__init__(self,name=name)
        self.urls =urls

    def run(self):
        print('Current %s is running....'%threading.current_thread().name)
        for url in self.urls:
            print('%s ----------->>>%s'%(threading.current_thread().name,url))
            time.sleep(random.random())
        print('%s ended....'%threading.current_thread().name)

if __name__=='__main__':
    print('%s us runing....'%threading.current_thread().name)
    t1=MyThread('Thread_1',['url_'+str(i) for i in range(10)])
    t2=MyThread('Thread_2',['url_'+str(i) for i in range(11,20)])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('%s ended.'%threading.current_thread().name)