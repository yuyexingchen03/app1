#!/usr/bin/env python
#coding:utf-8
import requests


class HtmlDownloader(object):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    def download(self,url):
        if url is None:
            return None
        headers ={'User-Agent',HtmlDownloader.user_agent}
        r =requests.get(url,headers =headers)
        if r.status_code ==200:
            r.encoding ='utf-8'
            return r.text
        return None
