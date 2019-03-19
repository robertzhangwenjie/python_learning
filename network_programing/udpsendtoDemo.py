# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2018/12/7 10:25
# File  :  udpsendtoDemo.py
# IDE   :  PyCharm

import socket

import sys


def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 获取对方的Ip/port
    dest_ip = input("请输入对方的ip:")
    dest_port = 7788
    try:
        dest_port = int(input("请输入对方的port:"))
    except Exception as e:
        print("输入的port有误")
    while True:
    # 从键盘获取数据
        send_data = input("请输入要发送的数据:")
        # 可以使用套接字收发数据 address 要是元组，包含ip和端口
        udp_socket.sendto(send_data.encode('utf-8'),(dest_ip,dest_port))

    # 关闭套接字
    udp_socket.close()
if __name__ == '__main__':
    main()

