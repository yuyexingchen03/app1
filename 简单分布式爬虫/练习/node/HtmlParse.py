#!/usr/bin/env python
#coding:UTF-8
# @Time     : 2018/4/18 8:35
# @Author   : zhengzhen
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self,page_url, content):
        if page_url is None or content is None:
            return None
        else:
            soup = BeautifulSoup(content,'lxml')
            new_urls = self.get_new_urls(page_url,soup)
            data = self.get_data(page_url,soup)
            return  new_urls,data

    def get_new_urls(self, page_url, soup):
        new_urls =set()
        alist = soup.find_all("a",href=re.compile(r'/item/.+'))
        for a in alist:
            href = a['href']
            full_href = urljoin(page_url,href)
            new_urls.add(full_href)
        return new_urls

    def get_data(self, page_url, soup):
        data ={}
        try:
            data['url'] =page_url
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




