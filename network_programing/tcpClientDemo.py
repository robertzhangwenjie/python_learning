# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/1/7 14:21
# File  :  tcpClientDemo.py
# IDE   :  PyCharm
import socket


def main():

    # 1.创建tcp的套接字
    # 参数理解:https://blog.csdn.net/zzyandzzzy/article/details/72236388
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.链接服务器
    server_ip =input("请输入要连接的服务器的ip:")
    server_port = int(input("请输入要链接的端口:"))
    server_addr = (server_ip,server_port)
    tcp_socket.connect(server_addr)

    # 3.发送数据/接收数据
    send_data = input("请输入要发送的数据:")
    tcp_socket.send(send_data.encode('utf-8'))



    # 4.关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()