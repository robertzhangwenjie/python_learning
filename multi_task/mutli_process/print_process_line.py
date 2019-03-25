# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/22 8:37
# File  :  print_process_line.py
# IDE   :  PyCharm
import time

for i in range(1, 101):
    time.sleep(0.5)
    print('\r当前进入为:%s%%' % i,end='')