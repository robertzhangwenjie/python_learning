# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/15 8:44
# File  :  global_variable.py
# IDE   :  PyCharm


'''
在一个函数中对全局变量进行修改的时候，如果只是修改了值，则不用使用global进行说明
如果修改了该变量指向的方向则需要进行说明
列如:
num = 123
def change():
    global num
    num += 100  此时因为使用了‘=’号，导致了num的指向发生了变化，因此需要加global num，不然报错

num_list = [1,2,3]
def change():
    num_list.append(4) 此时没有使用‘=’号，只是修改了num_list指向的数据值，因此不用加global
'''
num = 123
num_list = [1,2,3]

def change_num():
    global num
    num = 100

def change_num_list():
    num_list.append(4)

if __name__ == '__main__':
    print(num)
    change_num()
    print(num)
    change_num_list()
    print(num_list)
    print('{0}'.format())
