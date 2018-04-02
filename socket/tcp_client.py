#!/usr/bin/env python
#coding=utf-8
'''
TCP
客户端demo
'''
import socket
#初始化socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#链接目标的IP和端口
s.connect(('127.0.0.1',9999))
#接收消息
print('---->>>'+s.recv(1204).decode('utf-8'))
#发送消息
s.send(b'Hello, I am a client...')
print('---->>> '+s.recv(1024).decode('utf-8'))
s.send(b'exit')
#关闭socket
s.close()
