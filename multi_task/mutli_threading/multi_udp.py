# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/19 7:51
# File  :  multi_udp.py
# IDE   :  PyCharm
import socket


# AF_INET代表ipv4 SOCK_DGARM代表udp
# 1.创建套接字
import threading


# 5.接收数据
def recv(udp_socket):
    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)

def send(udp_socket,addr_ip,addr_port):
    # 发送数据
    while True:
        send_data = input("输入要发送的数据:")
        udp_socket.sendto(send_data.encode('utf-8'),(addr_ip,addr_port))

def main():
    '''
    完成udp聊天气的整体控制
    :return:
    '''
    # 1.创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定本地信息
    udp_socket.bind(("", 7890))

    # 3.获取接收方的ip和端口
    addr_ip = input("对方的ip:")

    # 注意端口要是int类型
    addr_port = int(input("对方的端口:"))

    # 4.创建两个线程用来同时进行接收和发送
    t_recv = threading.Thread(target=recv, args=(udp_socket,))
    t_send = threading.Thread(target=send, args=(udp_socket,addr_ip,addr_port))

    t_recv.start()
    t_send.start()




if __name__ == '__main__':
    main()