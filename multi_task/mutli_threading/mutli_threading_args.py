# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/18 8:21
# File  :  mutli_threading_variable.py
# IDE   :  PyCharm

# 定义一个全局变量
import threading
import time



def test1(tmp):
    tmp.append(44)
    print("test1 tmp=%s" % str(tmp))

def test2(tmp):
    print("test2 tmp=%s" % str(tmp))

g_nums = [11,22,33]
def main():
    # args 指定将来调用函数的时候传递什么数据过去，默认是空元祖()
    t1 = threading.Thread(target=test1,args=(g_nums,))
    t2 = threading.Thread(target=test2,args=(g_nums,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(2)

    print("main g_nums=%s" % str(g_nums))

if __name__ == '__main__':
    main()
