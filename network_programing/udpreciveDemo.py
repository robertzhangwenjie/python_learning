# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2018/12/7 13:31
# File  :  udpreciveDemo.py
# IDE   :  PyCharm

from socket import *

# 创建udp套接字
# AF_INET 代表使用IPV4进行通信
udp_scoket = socket(AF_INET,SOCK_DGRAM)

# 绑定一个端口，如果不绑定会随机分配
local_addr = ('',7788) #ip地址和端口号，Ip一般不用写，表示本机的任何一个ip
udp_scoket.bind(local_addr)

# 等待接收方发送的数据
while True:
    recv_data = udp_scoket.recvfrom(1024)

    recv_msg = recv_data[0]
    send_addr = recv_data[1]
    # 显示接收到的数据
    print(send_addr)
    print(recv_data)
    print(recv_data[0].decode('utf-8'))

# 关闭套接字
udp_scoket.close()
