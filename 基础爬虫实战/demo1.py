#!/usr/bin/env python
#coding:utf-8
import codecs
from urllib.parse import urljoin

import requests
import time
from bs4 import BeautifulSoup
import re
'''
url管理器
'''
class UrlManager(object):
    def __init__(self):
        self.new_urls=set()#未爬取 URL集合
        self.old_urls=set()#已爬取URL集合

    def has_new_url(self):
        '''
        判断是否有未爬取的URL
        :return:
        '''
        return  self.new_urls_size()!=0

    def new_urls_size(self):
        '''
        获取未爬取url的数量
        :return:
        '''
        return len(self.new_urls)

    def get_new_url(self):
        '''
        获取一个未爬取的URL
        :return:
        '''
        new_url =self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self,url):
        '''
        添加新的URL到未爬取的集合中
        :param url:
        :return:
        '''
        if url is None:
            return
        if url not in self.new_urls and url not  in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        '''
        批量添加urls到未爬取列表
        :param urls:
        :return:
        '''
        if urls is None or len(urls) ==0:
            return
        for url in urls:
            self.add_new_url(url)

    def old_url_size(self):
        '''
        获取已经爬取url集合的大小
        :return:
        '''
        return len(self.old_urls)

'''
Html 下载器
'''
class HtmlDownloader(object):
    def download(self,url):
        '''
        根据url访问网页
        :param url:
        :return:
        '''
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        headers ={'User-Agent':user_agent}
        r = requests.get(url,headers=headers)
        if r.status_code ==200:
            r.encoding ='utf-8'
            return r.text
        return None

'''
Html 解析器
'''
class HtmlParser(object):
    def parser(self,page_url,html_cont):
        '''
        用于解析网页内容,抽取url和简介数据
        :param page_url: 下载页面的url
        :param html_cont: 下载的网页内容
        :return: 返回URL和解析以后的数据
        '''
        if page_url is None or html_cont is None:
            return
        soup =BeautifulSoup(html_cont,'lxml',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_data(self, page_url, soup):
        '''
        抽取简介数据
        :param page_url:
        :param soup:
        :return:
        '''
        data ={}
        data['url'] =page_url
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title
        summary =soup.find('div',class_='lemma-summary')
        #获取tag中包含的所有文本内容,包括子孙tag中的内容,并将结果最为Unicode字符串返回
        data['summary'] =summary.get_text()
        return data

    def _get_new_urls(self, page_url, soup):
        '''
        抽取新的url集合
        :param page_url:
        :param soup:
        :return:
        '''
        new_urls=set()
        #抽取符合要求的a标签
        links = soup.find_all('a',href =re.compile(r'/item/.+'))
        for link in links:
            #提取href属性
            new_url = link['href']
            #补全完整地址
            new_full_url = urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

'''
数据存储器
'''
class DataOutput(object):
    def __init__(self):
        self.datas=[]

    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout=codecs.open('baike.html','w','utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>'%data['url'])
            fout.write('<td>%s</td>'%data['title'])
            fout.write('<td>%s</td>'%data['summary'])
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
'''
爬虫调度器
'''
class SpiderMan(object):
    def __init__(self):
        self.manager =UrlManager()
        self.downloader =HtmlDownloader()
        self.paser = HtmlParser()
        self.output =DataOutput()

    def crawl(self,root_url):
        #添加入口url
        self.manager.add_new_url(root_url)
        #判断url管理器中是否有新的url,同事判断抓取了多少个url
        while (self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                #从url管理器中取出新的url
                url = self.manager.get_new_url()
                #html网页下载器瞎子啊
                html  =self.downloader.download(url)
                #解析网页
                new_urls,data = self.paser.parser(url,html)
                #将抽取的url保存到url管理器中
                self.manager.add_new_urls(new_urls)
                #将数据存储到文件中
                self.output.store_data(data)
                print('已经抓取%s个链接'%self.manager.old_url_size())
                time.sleep(0.3)
            except Exception as e:
                print(e)
        #将数据输出
        self.output.output_html()

if __name__ =='__main__':
    sp = SpiderMan()
    sp.crawl('https://baike.baidu.com/item/Python/407313')