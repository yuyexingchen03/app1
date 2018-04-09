#!/usr/bin/env python
#coding:utf-8
from multiprocessing.managers import BaseManager

from multiprocessing import Queue


class NodeControl(object):
    def __init__(self,url_q,result_q):
        self.url_q = url_q
        self.result_q = result_q
        BaseManager.register('get_url_q', callable=self.get_url_q)
        BaseManager.register('get_result_q', callable=self.get_result_q)
        addrss = ('127.0.0.1', 9001)
        self.m = BaseManager(address=addrss, authkey=b'baike')


    def get_url_q(self):
        return self.url_q

    def get_result_q(self):
        return self.result_q

    def start(self):
        self.m.get_server().forenver()

    def url_manager_proc(self,url):



if __name__ =='__main__':
    #控制器给节点发送url的队列
    url_q =Queue()
    #节点给控制器发送结果队列
    result_q =Queue()
    #服务器主进程 给 处理进程通信的队列

    n = NodeControl(url_q,result_q)

    #urlmanager处理进程



    n.start()