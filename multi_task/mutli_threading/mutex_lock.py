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
    # 上锁，如果之前没有被上锁，那么此时上锁成功
    # 如果上锁之前已经被上锁了，那么此时会堵塞在这里，直到这个锁被解开
    # 锁的代码越少越好
    for i in range(tmp):
        mutex.acquire()
        g_num += 1
        mutex.release()
    # unlock
    print("test1 tmp=%d" % g_num)

def test2(tmp):
    global g_num
    # 一把锁只能有一个线程对其进行上锁，当一个线程已经加锁了，那么其他线程
    # 必须要等到锁解开后才能上锁，相当于多个线程抢一把锁，谁抢到了谁就可以执行
    for i in range(tmp):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("test1 tmp=%d" % g_num)

# create a mutex lock,default value is no-locking
mutex = threading.Lock()


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
