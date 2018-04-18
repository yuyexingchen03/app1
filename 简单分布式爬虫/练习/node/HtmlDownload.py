#!/usr/bin/env python
#coding:UTF-8
# @Time     : 2018/4/17 17:36
# @Author   : zhengzhen

import requests

class HtmlDownLoader(object):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    def download(self, url):
        if url is None:
            return None
        headers ={'User-Agent':HtmlDownLoader.user_agent}
        r =requests.get(url,headers =headers)
        if r.status_code ==200:
            r.encoding ='utf-8'
            return r.text
        return None
