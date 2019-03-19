# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/18 8:21
# File  :  mutli_threading_variable.py
# IDE   :  PyCharm

# 定义一个全局变量
import threading
import time

tmp = 100

def test1():
    global tmp
    g_num += 1
    print("test1 g_num=%d"%g_num)

def test2():
    print("test2 g_num=%d" % tmp)

def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(2)

    print("main g_num=%d" % tmp)

if __name__ == '__main__':
    main()