#!/usr/bin/env python
# coding:UTF-8
# @Time     : 2018/4/17 17:15
# @Author   : zhengzhen

from multiprocessing.managers import BaseManager

import time

from 简单分布式爬虫.练习.node.HtmlDownload import HtmlDownLoader
from 简单分布式爬虫.练习.node.HtmlParse import HtmlParser


class BaseManage(object):
    pass


class SpiderWorker(object):

    def __init__(self):
        # 注册方法
        BaseManager.register("get_url_q")
        BaseManager.register("get_result_q")
        self.baseManager = BaseManager(address=('127.0.0.1', 9001), authkey=b'baike')
        self.baseManager.connect()
        self.task = self.baseManager.get_url_q()
        self.result = self.baseManager.get_result_q()
        self.htmlDownLoader = HtmlDownLoader()
        self.parser = HtmlParser()
        print('init over')

    def craw(self):
        # i = 0
        while True:
            try:
                # print(str(i))
                # i = i + 1
                if not self.task.empty():
                    url = self.task.get()
                    if url == 'end':
                        print("子节点接到通知结束爬取页面")
                        self.result.put({'new_urls': 'end', 'data': 'end'})
                        return
                    else:
                        print("开始爬取:%s" % url.encode('utf-8'))
                        content = self.htmlDownLoader.download(url)
                        new_urls, data = self.parser.parse(url, content)
                        print(new_urls)
                        self.result.put({'new_urls': new_urls, 'data': data})
                else:
                    time.sleep(0.1)
            except Exception as e:
                print(e)
                time.sleep(0.1)


if __name__ == '__main__':
    s = SpiderWorker()
    s.craw()
