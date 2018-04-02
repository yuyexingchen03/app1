#!/usr/bin/env python
#codiing=utf-8

import random
import time,threading
'''
线程同步
RLock锁
acquire获取锁
release释放锁

由于GIL的存在python的多线程比较鸡肋
适合于io密集操作
不适用cpu密集操作
'''
#创建锁
mylock =threading.RLock()
num =0
class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self,name=name)

    def run(self):
        global num
        while True:
            # mylock.acquire()#获取锁
            print('%s locked, number:%d'%(threading.current_thread().name,num))

            if num>=100:
                # mylock.release()
                print('%s released,number:%d'%(threading.current_thread().name,num))
                break
            num+=1
            time.sleep(random.random())
            print('%s released ,number:%d'%(threading.current_thread().name,num))
            # mylock.release()

if __name__ == '__main__':
    thread1 =MyThread('thread_1')
    thread2 =MyThread('thread_2')
    thread3 =MyThread('thread_3')
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()

