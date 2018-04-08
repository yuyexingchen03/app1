#!/usr/bin/env python
#coding:utf-8
'''
操作邮箱
    发送右键
'''
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

'''
编码收件人 防止乱码
'''
def _format_addr(s):
    name,addr =parseaddr(s)
    return formataddr((Header(name,'UTF-8').encode(),addr))
#发件人地址
from_addr ='1414701937@qq.com'
#邮箱密码
# password='mqsaersjoweshebi'
password='kxogygvixbomjcfb'
#收件人地址
to_addr='815808731@qq.com'
#QQ邮箱服务器地址
smtp_server ='smtp.qq.com'
#设置邮件信息
'''
构建右键正文 
    _subtype:plain 文本邮件  html邮件
'''
msg = MIMEText('Python爬虫运行异常,异常信息为遇到HTTP 403',_subtype='plain',_charset='utf-8')
msg['From'] =_format_addr('一号爬虫 <%s>'%from_addr)
msg['To'] =_format_addr('管理员 <%s>'%to_addr)
msg['Subject'] =Header('一号爬虫运行状态','UTF-8').encode()
#发送右键
server = smtplib.SMTP_SSL(smtp_server,465)
server.login(from_addr,password)#登录服务器
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()#退出登录