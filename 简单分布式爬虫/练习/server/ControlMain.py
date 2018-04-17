#!/usr/bin/env python
#coding:utf-8
from multiprocessing.managers import BaseManager

from multiprocessing import Queue, Process

import time

from 简单分布式爬虫.练习.server.UrlManage import UrlManager
from 简单分布式爬虫.练习.server.DataOutPut import DataOutputer


class NodeControl(object):
    def __init__(self,url_q,result_q):
        self.url_q = url_q
        self.result_q = result_q
        # 服务端注册方法,向网络暴露
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

    def url_manager_proc(self,url,url_q,conn_q):
        urlManage=UrlManager()
        urlManage.add_new_url(url)
        while True:
            while urlManage.has_new_url():
                new_url = urlManage.get_new_url()
                url_q.put(new_url)
                print("old_url=",new_url)
                if urlManage.get_old_urls_size>200:
                    # 通知爬虫结束爬取
                    url_q.put("end")
                    urlManage.saveProcess("new_urls.txt",urlManage.new_urls)
                    urlManage.saveProcess("old_urls.txt",urlManage.old_urls)
                    return
            try:
                if not conn_q.emoty():
                    urls = conn_q.get()
                    urlManage.add_new_urls(urls)
            except:
                time.sleep(0.1)

    def result_servlo_proc(self,result_q,conn_q,stoe_q):
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get()
                    if content['new_urls'] == 'end':
                        # 结果分析进程收到结束通知,退出进程
                        print("resultSeloveProcess stop...")
                        # 通知保存进程 停止工作
                        stoe_q.put("end")
                        return
                    else:
                        conn_q.put(content['new_urls'])#url为set类型
                        stoe_q.put(content['data'])#解析出来的数据为dict类型
                else:
                    time.sleep(0.1)
            except:
                time.sleep(0.1)

    def sotre_proc(self,stoe_q):
        output = DataOutputer()
        while True:
            if not stoe_q.empty():
                data = stoe_q.get()
                if data == 'end':
                    print("数据保存进程结束")
                    output.output_end()
                    return
                else:
                    output.store_data(data)
            else:
                time.sleep(0.1)



if __name__ =='__main__':
    #控制器给节点发送url的队列
    url_q =Queue()
    #节点给控制器发送结果队列
    result_q =Queue()
    #服务器主进程 给 处理进程通信的队列
    # 要保存处理的url列表
    conn_q = Queue()
    # 要序列化的爬取数据
    stoe_q =Queue()

    n = NodeControl(url_q,result_q)
    root_url = "https://baike.baidu.com/item/java/85979"
    #urlmanager处理进程
    ulrProce = Process(target=n.url_manager_proc,name='urlManageProcess',args=(root_url,url_q,conn_q))
    # 处理节点发过来的数据的进程
    resultProcess = Process(target=n.result_servlo_proc,name="resultProcess",args=(result_q,conn_q,stoe_q))
    # 保存数据进程
    storeProcess = Process(target=n.sotre_proc,name="sotreProcess",args=(stoe_q,))

    n.start()