#!/usr/bin/env python
#codiing=utf-8

import random
import time,threading
'''
线程执行taeget方法运行线程
'''

#新线程执行的代码
def thread_run(urls):
    print('Current %s is running...'%threading.current_thread().name)
    for url in urls:
        print('%s------------->>> %s'%(threading.current_thread().name,url))
        time.sleep(random.random())
    print('%s ended.'%threading.current_thread().name)

print('%s is running...'%threading.current_thread().name)
t1=threading.Thread(target=thread_run,name='Thread_1',args=(['url_'+str(i) for i in range(10)],))
t2=threading.Thread(target=thread_run,name='Thread_2',args=(['url_'+str(i) for i in range(11,20)],))
t1.start()
t2.start()
t1.join()
t2.join()
print('%s is eneed.'%threading.current_thread().name)
