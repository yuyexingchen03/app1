#!/usr/bin/env python
from multiprocessing import  Process,Queue
import os ,time,random
'''
多进程Queue通信
'''
#写数据进程执行的代码
def pro_write(q,urls):
    print('Process(%s) is writing...'%os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...'%url)
        time.sleep(random.randint(1,4))

#读数据进程执行的代码:
def proc_reader(q):
    print('Process(%s) is reading...' % os.getpid())
    while True:
        url =q.get(True)
        print('Get %s from queue.' %url)

if __name__=='__main__':
    #父进程创建Queue ,并传递给各个子进程
    q =Queue()
    pro_write1 = Process(target=pro_write,args=(q,['url1','url2','url3']))
    pro_write2 = Process(target=pro_write,args=(q,['url4','url5','url6']))
    pro_read =Process(target=proc_reader,args=(q,))
    #启动子进程pro_writer 写入:
    pro_write1.start()
    pro_write2.start()
    #启动子进程Pro_reader,读取:
    pro_read.start()
    #等待proc_writer结束
    pro_write1.join()
    pro_write2.join()
    #proc_reader 进程是死循环,无法等待期结束,只能强行终止
    pro_read.terminate()
