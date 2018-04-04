#!/usr/bin/env python
#coding=utf-8
'''
UDP
服务端demo
'''
import socket
import threading
import time
#创建 Socket ,绑定指定的IP和端口
#Sock_DGRAM指定了这个Socket的类型是UDP,绑定端口和TCP示例是一样的
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999')
while True:
    #直接发送数据和接收数据
    data,addr = s.recvfrom(1024)
    print('Received from %s:%s.'%addr)
    s.sendto(b'Hello,%s!'%data,addr)