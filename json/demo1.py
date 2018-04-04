#!/usr/bin/env python
#coding::utf-8
import requests
from bs4 import BeautifulSoup
user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36";
header={"User-Agent":user_agent}
url ='http://seputu.com/'
r =requests.get(url,headers=header)
soup = BeautifulSoup(r.text,'lxml')
for muluDiv in soup.find_all(class_='mulu'):
    h2 = muluDiv.find('h2')
    if h2:
        muluTitle = h2.string
        for a in muluDiv.find(class_='box').find_all('a'):
            href = a['href']
            sectionTitle = a.string
            print('章节<%s>--->单元<%s><%s>'%(muluTitle,sectionTitle,href))




