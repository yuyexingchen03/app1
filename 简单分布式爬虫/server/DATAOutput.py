#!/usr/bin/env python
#coding:utf-8
import codecs
import time


class DataOutPut(object):
    def __init__(self):
        self.filepath ='baike_%s.html'%(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime()))
        self.output_head(self.filepath)
        self.datas=[]

    def store_data(self,data):
        '''
        爬取的数据先保存到内存中
        当超过10条数据,就本地化保存一次
        :param data:
        :return:
        '''
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas)>10:
            self.output_html(self.filepath)

    def output_head(self, path):
        '''
        将html头写进去
        :param filepath:
        :return:
        '''
        fout= codecs.open(path,'w','utf-8')
        fout.write('<html>')
        fout.write('<head>')
        fout.write('<title>')
        fout.write(u'爬取百度百科')
        fout.write('</title>')
        fout.write('</head>')
        fout.write('<body>')
        fout.close()

    def output_html(self, filepath):
        '''
        将数据写入到html文件
        :param filepath:
        :return:
        '''
        fout = codecs.open(filepath,'a','utf-8')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>'%data['url'])
            fout.write('<td>%s</td>'%data['title'])
            fout.write('<td>%s</td>'%data['summary'])
            fout.write('</tr>')
            self.datas.remove(data)
        fout.close()

    def output_end(self,path):
        '''
        写入html结束标签
        :param path:
        :return:
        '''
        fout = codecs.open(path,'a','utf-8')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()