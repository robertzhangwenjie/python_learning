# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/22 8:45
# File  :  iteration.py
# IDE   :  PyCharm

from collections import Iterable,Iterator


class Classmate(Iterable):
    def __init__(self):
        self.names = list()

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
        return ClassIterator(self)

    def __next__(self):
        pass

    def __repr__(self):
        return str(self.names)

class ClassIterator():
    def __init__(self,obj):
        self.obj = obj
        # 定义迭代器的属性number，用来计算调用次数
        self.number = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.number < len(self.obj.names):
            # 返回其第number次调用的值
            ret = self.obj.names[self.number]
            # 每次调用后加1
            self.number += 1
            return ret
        else:
            raise StopIteration
classmate = Classmate()
# iter调用classmate的__iter__方法，属于内置python的方法



# for i in classmate:
#     print(i)

# 判断一个对象是否可以用for进行迭代
# 1.判断对象是否可以迭代 isinstance(obj,Iterable)，也就是该对象是否局域__iter__方法
print('判断是否可以迭代:',isinstance(classmate,Iterable))
# 2.在第一步的前提下，调用iter(obj)方法得到obj对象的__iter__方法的返回值,判断是否是迭代器
classmate_iterator = iter(classmate)
print(isinstance(classmate_iterator,Iterator))
# 3.使用函数next方法调用迭代器中的__next__方法
print(next(classmate_iterator))

