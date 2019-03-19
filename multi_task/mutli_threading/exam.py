# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/18 14:17
# File  :  exam.py
# IDE   :  PyCharm

# title:创建两个线程，其中一个输出1-52，另外一个输出A-Z。输出格式要求：12A 34B 56C 78D

'''
解题思路:
1.一个线程打印12，另一个线程打印A-Z加上一个空格' '，且打印的时候不换行
2.需要顺序执行，则需要利用锁来管理依赖关系，创建两个锁，第一个线程执行需要等待第二个线程
    释放第一个锁，同时第一个线程执行完时需要释放第二个线程需要获取的锁，第二个线程执行需
    要等待第一个线程释放完锁
3.第一个线程必须先执行
'''
import threading


def show1():
    for i in range(1,53,2):
        # 获取线程2的锁
        lock_show2.acquire()
        print(i,end='')
        print(i+1,end='')
        #打印一个循环后，释放第二个线程运行需要的锁
        lock_show1.release()



def show2():
    for i in range(65,91):
        # 只有获取了第一个线程释放的锁，才能开始执行
        lock_show1.acquire()
        print(chr(i),end=' ')
        # 释放第1个线程执行需要获取的锁
        lock_show2.release()

lock_show1 = threading.Lock()
lock_show2 = threading.Lock()

def main():
    t1 = threading.Thread(target=show1)
    t2 = threading.Thread(target=show2)

    # 保证第一个线程能够运行，必须要先获取show1锁，不然线程1中无法释放show1锁
    lock_show1.acquire()
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()

