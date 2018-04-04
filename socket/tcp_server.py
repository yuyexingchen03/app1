#!/usr/bin/env python
#coding=utf-8
'''
TCP
服务端demo
'''
import socket
import threading
import time
def dealClient(sock,addr):
    #第四步:接受传来的数据,并发送给对方数据
    print('Accept new connection from %s:%s...' %addr)
    sock.send(b'Hello,I am TCP server...')
    while True:
        data =sock.recv(1024)#接受数据
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('----->>>%s!' % data.decode('utf-8'))
        sock.send(('Loop_Msg : %s!'% data.decode('utf-8')).encode('UTF-8'))
    #第五步 关闭socket
    sock.close()
    print('Connection from %s:%s closed.'%addr)

if __name__ == '__main__':
    #第一步: 创建一个基于IPv4和TCp协议的socket
    #socket绑定的Ip(127.0.0.1为本机IP)与端口
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',9999))
    #第二步:监听链接
    s.listen(5)
    print('Waiting for connection....')
    while True:
        #第三步:接收一个新连接:
        sock,addr = s.accept()
        #创建新线程 来处理TCP处理
        t =threading.Thread(target=dealClient,args=(sock,addr))
        t.start()