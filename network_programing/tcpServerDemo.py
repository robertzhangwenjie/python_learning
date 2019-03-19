# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/1/9 17:39
# File  :  tcpServerDemo.py
# IDE   :  PyCharm

import socket


def main():
    # 1.创建socket
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.绑定端口
    tcp_addr = ('127.0.0.1',1200)
    tcp_server_socket.bind(tcp_addr)

    # 3.开启监听,让套接字变为被动套接字
    tcp_server_socket.listen(128)

    # 4.等待客户端的链接
    client_scoket,clientAddr = tcp_server_socket.accept()

    # 5.接收数据
    recv_data = tcp_server_socket.recv(1024) # 接收1024个字节
    print(recv_data.decode('utf-8'))

    # 6.发送一些数据到客户端
    client_scoket.send("thank you!".encode('utf-8'))

    # 7.关闭为这个客户端服务的套接字，只要关闭了，就不再为这个客户端服务
    client_scoket.close()
if __name__ == '__main__':
    main()