# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/20 7:59
# File  :  mutli_process_demo.py
# IDE   :  PyCharm
import threading
import multiprocessing

def test1():
    print('---test1---')

def test2():
    print('---test2---')

def main():
    # t1 = threading.Thread(target=test1)
    t1 = multiprocessing.Process(target=test1)
    # t2 = threading.Thread(target=test2)
    t2 = multiprocessing.Process(target=test2)

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()