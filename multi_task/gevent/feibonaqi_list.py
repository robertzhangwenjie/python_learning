# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/25 8:30
# File  :  feibonaqi_list.py
# IDE   :  PyCharm



class Feibonaci(object):

    def __init__(self,nums):
        self.nums = nums
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current_num < self.nums:
            ret = self.a
            self.a,self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration



a = [11,22,33]
t = (11,22,33)

print(list(t))
print(tuple(a))