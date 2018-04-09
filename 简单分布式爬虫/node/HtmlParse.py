#!/usr/bin/env python
#coding:utf-8
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import  re

class HtmlParser(object):
    def parse(self,page_url,html_content):
        '''
        用于解析网页内容, 抽取url和数据
        :param page_url:
        :param html_content:
        :return:
        '''

        if page_url is None or html_content is None:
            return
        soup =BeautifulSoup(html_content,'lxml')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 抽取符合要求的a标签
        links = soup.find_all('a', href=re.compile(r'/item/.+'))
        for link in links:
            # 提取href属性
            new_url = link['href']
            # 补全完整地址
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        '''
        抽取简介数据
        :param page_url:
        :param soup:
        :return:
        '''
        data = {}
        try:
            data['url'] = page_url
            title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()
            data['title'] = title
            summary = soup.find('div', class_='lemma-summary')
            if summary is not None:
                # 获取tag中包含的所有文本内容,包括子孙tag中的内容,并将结果最为Unicode字符串返回
                data['summary'] = summary.get_text()
            else:
                data['summary'] = 'None'
        except:
            return None

        return data
