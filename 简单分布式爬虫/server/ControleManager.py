#!/usr/bin/env python
#coding:utf-8
'''
节点管理器
'''
from multiprocessing.managers import BaseManager

import time

from multiprocessing import Queue, Process

from 简单分布式爬虫.server.DATAOutput import DataOutPut
from 简单分布式爬虫.server.URLManager import UrlManager


class NodeManager(object):

    def get_url_q(self):
        return self.url_q

    def get_result_q(self):
        return self.result_q

    def start_Manager(self,url_q,result_q):
        self.url_q =url_q
        self.result_q =result_q
        '''
        创建一个分布式管理器
        :param url_q:  url队列
        :param result_q: 结果队列
        :return: 
        '''
        #把创建的两个队列注册在网络上,利用register方法,callable参数关联了Queue对象
        #把Queue对象在网络中暴露
        # BaseManager.register('get_task_queue',callable=lambda :url_q)
        # BaseManager.register('get_result_queue',callable=lambda :result_q)
        BaseManager.register('get_task_queue',callable=self.get_url_q)
        BaseManager.register('get_result_queue',callable=self.get_result_q)
        #绑定端口 8002 设置验证口令'baike'.这个相当于对象的初始化
        manager = BaseManager(address=('127.0.0.1',8002),authkey=b'baike')
        #返回manager对象
        return manager

    '''
        URL管理进程将从conn_q队列获取到新的URL提交给URL管理器,经过去重之后,取出URL放入url_queue
        队列中传递给爬虫节点
    '''
    def url_manager_proc(self,url_q,conn_q,root_url):
        url_manager =UrlManager()
        url_manager.add_new_url(root_url)
        while True:
            while url_manager.has_new_url():
                #从url管理器中获取新的url
                new_url = url_manager.get_new_url()
                #将新的url发给工作节点
                url_q.put(new_url)
                print('old_url=',url_manager.old_url_size())
                #加一个判断条件,当爬取2000个链接后就关闭,并保存进度
                if(url_manager.old_url_size()>200):
                    #通知爬行节点工作结束
                    url_q.put('end')
                    print('控制节点发起结束通知!')
                    #关闭管理节点 ,同时存储set状态
                    url_manager.save_progress('new_urls.txt',url_manager.new_urls)
                    url_manager.save_progress('old_urls.txt',url_manager.old_urls)
                    return
                #将从result_solve_proc获取到的url添加到url管理器
                try:
                    if not conn_q.empty():
                        urls = conn_q.get()
                        url_manager.add_new_urls(urls)
                except BaseException as e:
                    time.sleep(0.1)#延时休息
    '''
    数据提取进程从result_queue队列读取返回的数据,并将数据中url添加到conn_q队列交给url管理进程,
    将数据中的文章标题和摘要添加到store_q队列交给数据存储进程
    '''
    def result_solve_proc(self,result_q,conn_q,store_q):
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        #结果分析进程接收到结束通知,结束进程
                        print('结果分析进程接收到通知结束!')
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])#url为set类型
                    store_q.put(content['data'])#解析出来的数据为dict类型
                else:
                    time.sleep(0.1)#延时休息
            except Exception as e:
                time.sleep(0.1)#延时休息

    '''
    数据存储进程从store_q队列中读取数据,并调用数据存储器进行数据存储
    '''
    def store_proc(self,store_q):
        output = DataOutPut()
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data =='end':
                    print('存储进程接收通知然后结束!')
                    output.output_end(output.filepath)
                    return
                output.store_data(data)
            else:
                time.sleep(0.1)

'''
最后启动分布式管理器 url管理器 数据提取进程和数据存储进程
'''
if __name__ =='__main__':
    #初始化4个队列
    url_q = Queue()# url管理进程 将url传递给爬虫节点的通道
    result_q = Queue() #是爬虫节点将数据返回给数据提取进程的通道
    store_q =Queue() #是数据提取进程将获取到的数据交给数据存储进程的通道
    conn_q = Queue()#是数据提取进程将新的url数据提交给url管理进程的通道
    #创建分布式管理器
    node =NodeManager()
    manager = node.start_Manager(url_q,result_q)
    # 创建URL管理进程 数据提取进程 和数据存储进程
    root_url='https://baike.baidu.com/item/Python/407313'
    #将conn_q中的url和root_url放到url_q中
    url_manager_proc = Process(target=node.url_manager_proc,args=(url_q,conn_q,root_url))
    # 将result_q中的数据解析到conn_q和store_q中
    result_solve_proc =Process(target=node.result_solve_proc,args=(result_q,conn_q,store_q))
    #将store_q中的数据保存到文件中
    store_proc = Process(target=node.store_proc,args=(store_q,))
    #启动3个进程 和分布式管理器
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    manager.start()
