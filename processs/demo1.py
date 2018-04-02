#!/usr/bin/env python
import os
from multiprocessing import Process
'''
通过Process创建进程
'''
#紫禁城 要执行的代码
def run_proc(name):
    print('Child process %s (%s) Running...'%(name,os.getpid()))

if __name__ == '__main__':
    print('parent process %s'%os.getpid())
    for i in range(5):
        p =Process(target=run_proc,args=(str(i),))
        print('Process will start')
        p.start()
        p.join()
    print('Process end.')