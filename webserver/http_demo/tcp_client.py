# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/4/1 10:38
# File  :  tcp_client.py
# IDE   :  PyCharm

import socket

# 新建一个socket套接字
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 链接服务器
host = '127.0.0.1'
port = 7890
tcp_socket.connect((host,port))

# 发送数据
data = 'abc'

tcp_socket.send(data.encode('utf-8'))

# 接收服务端回复
recv_data = tcp_socket.recv(1024)
print(recv_data)

# 关闭套接字
tcp_socket.close()