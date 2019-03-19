# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/18 8:21
# File  :  mutli_threading_variable.py
# IDE   :  PyCharm

# 定义一个全局变量
import threading
import time

g_num = 0

def test1(tmp):
    global g_num
    for i in range(tmp):
        g_num += 1
    print("test1 tmp=%d" % g_num)

def test2(tmp):
    global g_num
    for i in range(tmp):
        g_num += 1
    print("test1 tmp=%d" % g_num)

def main():
    # args 指定将来调用函数的时候传递什么数据过去，默认是空元祖()
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))

    t1.start()
    t2.start()
    time.sleep(2)

    print("main g_nums=%d" % g_num)

if __name__ == '__main__':
    main()
