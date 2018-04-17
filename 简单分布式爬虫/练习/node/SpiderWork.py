#!/usr/bin/env python
#coding:UTF-8
# @Time     : 2018/4/17 17:15
# @Author   : zhengzhen

from multiprocessing.managers import BaseManager

class BaseManage(object):
    pass


class SpiderWorker(object):

    def __init__(self):
        # 注册方法
        BaseManager.register("get_url_q")
        BaseManager.register("get_result_q")
        self.baseManager = BaseManager(address=('192.168.100.163',9001),authkey=b'baike')
        self.baseManager.connect()
        self.task = self.baseManager.get_url_q()
        self.result = self.baseManager.get_result_q()
        self.htmlDownLoader = HtmlDownLoader()
