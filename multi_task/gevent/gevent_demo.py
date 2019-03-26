# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/26 8:12
# File  :  gevent_demo.py
# IDE   :  PyCharm
import time
import  random
from gevent import monkey
import gevent


# 添加补丁，将程序中用到的耗时操作的代码，换为gevent中自己实现的模块
# 实现原理:将代码copy到一个区域，将耗时操作修改为gevent中的耗时再执行
monkey.patch_all()
def f1(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        # 协程使用的是gevent库中的网络库，因此遇到time时并不会认为是耗时
        # 如果想协程认为是耗时，需要打补丁:monkey.patch_all()
        time.sleep(random.random())
        # 添加协程中的耗时，让协程进行切换
        # gevent.sleep(0.5)

def f2(n):
    for i in range(n):
        # 获取当前的协程
        print(gevent.getcurrent(),i)
        time.sleep(random.random())
        # gevent.sleep(0.5)

def f3(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        time.sleep(random.random())
        # gevent.sleep(0.5)

# spawn为生成gevent对象，参数1位函数名，参数2为函数的参数

# g1 = gevent.spawn(f1,5)
# g2 = gevent.spawn(f2,5)
# g3 = gevent.spawn(f3,5)

# 等待G1执行完毕
# gevent的一大特点:遇到耗时会开始切换执行
# 列如: g1执行后没有立马完成或者遇到耗时，此时g2会开始执行，g2中也有耗时，此时会切换到
# g3,此时就实现了广义的并发执行了
# g1.join()
# g2.join()
# g3.join()

# 更简洁的方式加入协程
gevent.joinall([
    gevent.spawn(f1,5),
    gevent.spawn(f2,5),
    gevent.spawn(f3,5)
])