# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/15 8:26
# File  :  multi_threading_practise.py
# IDE   :  PyCharm
import threading


def read():
    print('reading....')

def write():
    print('writing...')

def main():
    t1 = threading.Thread(target=read)
    t2 = threading.Thread(target=write)
    t1.start()
    t2.start()

class ComReadWrite(threading.Thread):
    def run(self):
        read()
        write()

if __name__ == '__main__':

    for i in range(5):
        # t3 = ComReadWrite()
        # t3.start()

        # 使用继承Thread类和普通的函数来new对象都是可以的
        main()