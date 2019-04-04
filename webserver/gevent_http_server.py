# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/4/3 8:14
# File  :  multiprocess_http_server.py
# IDE   :  PyCharm
import time

import gevent
import random
from gevent import monkey
monkey.patch_all()
import socket
import re




# 解析request
def get_request_data(request):
    request_dict = {}
    request_value = re.match(r'([^/]+)\s(/.*)\s(.*)',request)
    # 判断是否可以匹配
    if request_value:
        request_dict['method'] = request_value.group(1).upper()
        # print(request_dict['method'])
        request_dict['uri'] = request_value.group(2)
        # print(request_dict['uri'])
        request_dict['http_version'] = request_value.group(3)
        # print(request_dict['http_version'])
        # print(request_value.group(1))
    else:
        raise ValueError('请求错误')
    return request_dict

# 服务客户端
def serve_socket(client_socket):
    recv = client_socket.recv(1024)

    # 把接收到的数据进行解码
    recv_data = recv.decode('utf-8')
    print(recv_data)
    recv_lines = recv_data.splitlines()

    # 如果有请求数据，则获取
    file_name = ''

    if recv_lines:
        request_method = get_request_data(recv_lines[0])['method']
        # print(request_method)
        request_uri = get_request_data(recv_lines[0])['uri']

        # print(request_uri)
        # 如果请求的uri为/则默认返回index.htnl
        if request_uri == '/':
            file_name = '/index.html'
        else:
            file_name = request_uri

    # 需要返回的数据
    send_data = 'HTTP/1.1 200 OK\r\n'
    # 返回头部信息
    send_data += 'Content-Type: text/html;charset=UTF-8\r\n'
    send_data += "\r\n"


    # 需要返回的body
    html_content = ''
    try:
        with open('.'+file_name,'rb') as f:
            html_content = f.read()
        client_socket.send(send_data.encode('utf-8'))
        client_socket.send(html_content)
    except Exception as e:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += '\r\n'
        response += '404 NOT FOUND'
        client_socket.send(response.encode('utf-8'))
    # 发送数据

    client_socket.close()
    time.sleep(random.random())

# tcp服务器
def main():
    # 创建一个tcp套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 使该socket可以复用端口
    tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 绑定一个端口
    tcp_socket.bind(("",7890))

    # 将套接字变为监听套接字,backlog决定socket队列的长度
    tcp_socket.listen(128)

    # 等待客户端链接
    # 注意：accept()函数会返回一个元组
    # 元素1为客户端的socket对象，元素2为客户端的地址(ip地址，端口号)


    # 为客户端服务
    while True:
        client_socket, client_addr = tcp_socket.accept()
        # 采用多进程来接收客户端的请求

        t1 = gevent.spawn(serve_socket,client_socket)
        # t2 = gevent.spawn(serve_socket,client_socket)
        t1.join()
        # t2.join()

        # gevent.joinall([
        #     gevent.spawn(serve_socket, client_socket),
        # ])




        # serve_socket(client_socket)

if __name__ == '__main__':
    main()
