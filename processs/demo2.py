#!/usr/bin/env python
import os,time,random
from multiprocessing import  Pool
'''
通过pool进程池创建多个进程
'''
def run_task(name):
    print('Task %s (pid =%s) is running,,,'%(name,os.getpid()))
    time.sleep(random.random()*3)
    print('Task %s end.'%name)

if __name__ =='__main__':
    print('Current process %s.'%os.getpid())
    p =Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task,args=(i,))
    print('Waiting for all subprocesses dome...')
    p.close()
    p.join()
    print('Allsubprocesses done.')
