#!/usr/bin/env python
#coding:UTF-8
# @Time     : 2018/4/17 16:55
# @Author   : zhengzhen
import time
import codecs

class DataOutputer(object):

    def __init__(self):
        self.filePath="baike_%s.html"%(time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime()))
        self.output_head()
        self.datas=[]

    def output_head(self):
        with codecs.open(self.filePath,'a+',encoding="utf-8") as f:
            f.write("<html>")
            f.write("<head>")
            f.write("<title>")
            f.write("爬取JAVA相关百度百科页面数据")
            f.write("</title>")
            f.write("</head>")
            f.write("<body>")
            f.write("<table>")

    def output_end(self):
        with codecs.open(self.filePath,'a+',encoding="utf-8") as f:
            f.write("</table>")
            f.write("</body>")
            f.write("</html>")

    def sto_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas)>10:
            self.output_content()

    def output_content(self):
        with codecs.open(self.filePath,'a+',encoding='utf-8') as f:
          for data in self.datas:
              f.write("<tr>")
              f.write("<td>")
              f.write(data['url'])
              f.write("</td>")
              f.write("<td>")
              f.write(data['title'])
              f.write("</td>")
              f.write("<td>")
              f.write(data['content'])
              f.write("</td>")
              f.write("</tr>")

