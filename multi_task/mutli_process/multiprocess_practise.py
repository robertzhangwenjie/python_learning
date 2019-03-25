# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/20 9:31
# File  :  multiprocess_practise.py
# IDE   :  PyCharm

import multiprocessing


def write(article):
    writing_list = [1,2,3,4]
    for i in writing_list:
        article.put(i)
        print('写入%s'%i)
    print('写入完成')
    

def read(article):
    reading_list = list()
    while True:
        reading = article.get()
        reading_list.append(reading)
        print('读取%s'%reading)
        # 判断队列是否为空
        if article.empty():
            break
    print('读取完成')

def main():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=write,args=(q,))
    p2 = multiprocessing.Process(target=read,args=(q,))

    p1.start()
    p2.start()

if __name__ == '__main__':
    main()
