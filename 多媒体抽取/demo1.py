#!/usr/bin/env python
#coding:utf-8
from urllib.request import urlretrieve

import requests
import time
from bs4 import BeautifulSoup
import urllib
'''
下载进度函数
'''
def Schedule(blocknum,blocksize,totalsize):
    '''

    :param blocknum: 已经下载的数据块数量
    :param blocksize: 数据块大小
    :param totalsize: 远程文件的大小
    :return:
    '''
    per = 100.0 * blocknum*blocksize/totalsize
    if per>100:
        per =100
        print('当前下载进度:%d'%per)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers ={'User-Agent':user_agent}
url= 'http://www.ivsky.com/tupian/ziranfengguang/'
r =requests.get(url,headers=headers)
soup = BeautifulSoup(r.text,'lxml')
imgDivList = soup.find_all('div',class_='il_img')
i = 0
for imgDiv in imgDivList:
    img = imgDiv.find('img')
    if img:
        urlretrieve(img['src'],'img-'+str(i)+'.jpg',Schedule)
        # time.sleep(0.5)
        # imgR = requests.get(img['src'],headers=headers)
        # with open('img-'+str(i)+'.jpg','wb') as f:
        #     i =i+1
        #     f.write(imgR.content)