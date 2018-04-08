#!/usr/bin/env python
#coding:utf-8
import codecs
import hashlib
import pickle


class UrlManager(object):
    def __init__(self):
        #未爬取URL集合
        self.new_urls =self.load_progress('new_urls.txt')
        #已爬取url集合
        self.old_urls = self.load_progress('old_urls.txt')

    def has_new_url(self):
        '''
        判断是否有未爬取的url
        :return:
        '''
        return self.new_url_szie()!=0
    def get_new_url(self):
        '''
        获取一个未爬取的url
            并将该url的md5值放到已经爬取的url集合中
        :return:
        '''
        new_url = self.new_urls.pop()
        #此处md5摘要算法返回的是一个256位数字,我们只取中间128位
        m = hashlib.md5()
        m.update(new_url.encode('utf-8'))
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url

    def add_new_url(self,url):
        '''
        将新的url添加到未爬取集合
        :param url:
        :return:
        '''
        if url is None:
            return
        m =hashlib.md5()
        m.update(url.encode('utf-8'))
        url_md5 =m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        '''
        批量添加
        :param urls:
        :return:
        '''
        if urls is None or len(urls) ==0:
            return
        for url in urls:
            self.add_new_url(url)

    def load_progress(self, param):
        pass

    def new_url_szie(self):
        '''
        获取未爬取url集合的大小
        :return:
        '''
        return len(self.new_urls)

    def old_url_size(self):
        '''
        获取已经爬取url集合大小
        :return:
        '''
        return len(self.old_urls)

    def save_progress(self,path,data):
        '''
        保存爬取进度
        :param path:
        :param data:
        :return:
        '''
        with open(path,'wb') as fp:
            pickle.dump(data,fp)#对象序列化

    def load_progress(self,path):
        '''
        从本地序列化文件中加载进度
        :param path:
        :return:
        '''
        print('[+] 从文件加载进度: %s'%path)
        try:
            with open(path,'rb') as fp:
                tmp = pickle.load(fp)
                return tmp
        except Exception as e:
            print('[!] 无进度文件, 创建:%s'%path)
        return set()