# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/21 7:48
# File  :  pool.py
# IDE   :  PyCharm
'''
在利用Python进行系统管理的时候，特别是同时操作多个文件目录，或者远程控制多台主机，
并行操作可以节约大量的时间。当被操作对象数目不大时，可以直接利用multiprocessing中
的Process动态成生多个进程，十几个还好，但如果是上百个，上千个目标，手动的去限制进
程数量却又太过繁琐，此时可以发挥进程池的功效。
Pool可以提供指定数量的进程供用户调用，当有新的请求提交到pool中时，如果池还没有满，
那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那
么该请求就会等待，直到池中有进程结束，才会创建新的进程来它。
'''
import multiprocessing


def worker(num):
    print(num*num)

def main():
    # 创建一个允许有最多4个进程的进程池
    po = multiprocessing.Pool(4)

    for i in range(10):
        # 往进程池中添加任务
        po.apply_async(worker,args=(i,))

    print('---start---')
    # 关闭进程池，关闭后po不再接收新的请求
    po.close()
    # 等待po中所有子进程执行完成，必须放在close语句后
    po.join()
    print('---end---')

if __name__ == '__main__':
     print(multiprocessing.cpu_count())