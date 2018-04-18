#!/usr/bin/env python
# coding:utf-8

import os
import pickle
import codecs


class UrlManager(object):

    def __init__(self):
        self.new_urls = self.load_process("new_urls.txt")
        self.old_urls = self.load_process("old_urls.txt")

    def add_new_url(self, url):
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        return len(self.new_urls) > 0

    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

    def saveProcess(self, path, new_urls):
        '''
        保存进度
        :param param:
        :param new_urls:
        :return:
        '''
        with open(path, 'wb') as f:
            pickle.dump(path, f)

    def load_process(self, path):
        '''
        加载进度文件
        :param path:
        :return:
        '''
        print("[+]从文件加载进度: %s" % path)
        try:
            with open(path, 'rb') as f:
                tmp = pickle.loadf(f)
                return tmp
        except Exception as e:
            print("无进度文件,创建:%s" % path)
        return set()

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_old_urls_size(self):
        return len(self.old_urls)
