# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/14 11:03
# File  :  multi_threading.py
# IDE   :  PyCharm
import time
import threading


def sing():
    for i in range(5):
        print('''---singing...%d'''%i)
        time.sleep(1)

def dance():
    for i in range(5):
        print('''---dancing---%d'''%i)
        time.sleep(1)

def main():
    # create a thread
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    # start thread
    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        print('the count of running thread currently is:%d'%length)
        # print(threading.enumerate())
        if length <=1:
            break
        time.sleep(0.5)

class MyThread(threading.Thread):
    '''
    当使用类继承Thread类时，如果调用方法start时，会默认执行该类中的run方法
    使用场景:
     当一个比较负责的场景需要用到多线程时，可以采用类封装的形式列如:
    '''
    def run(self):
        for i in range(4):
            self.test()
            print('test class mythread')


    def test(self):
        print('test')




if __name__ == '__main__':
    t = MyThread()
    t.start()