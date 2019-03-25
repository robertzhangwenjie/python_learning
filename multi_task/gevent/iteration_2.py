# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/22 8:45
# File  :  iteration.py
# IDE   :  PyCharm

from collections import Iterable,Iterator


class Classmate(Iterable):
    def __init__(self):
        self.names = list()
        self.current_number =0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        '''
        如果想要一个对象成为一个可以迭代的对象，即可以使用for，
        那么必须要实现__iter__方法,且返回具有__next__方法的对象的引用
        使用for循环进行迭代时，会调用__iter__方法返回对象中的__next__方法
        该对象其实就是迭代器,迭代器中必须拥有__next__和__iter__方法
        :return:
        '''
        return self

    def __next__(self):
        if  self.current_number < len(self.names):
            ret =  self.names[self.current_number]
            self.current_number += 1
            return ret
        else:
            raise StopIteration

    def __repr__(self):
        return str(self.names)



classmate = Classmate()
classmate.add(1)
classmate.add(2)
classmate.add(3)
classmate.add(4)
classmate.add(5)

for i in classmate:
    print(i)

