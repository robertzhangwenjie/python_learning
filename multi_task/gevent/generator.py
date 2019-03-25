# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/25 9:08
# File  :  generator.py
# IDE   :  PyCharm

# 生成器是一种特殊的迭代器，可以进行迭代

# 用函数(生成器)实现斐波那契数列
# def gen(nums):
#     a, b = 0, 1
#     current_num = 0
#     while current_num < nums:
#         yield a     #如果一个函数中有yield语句，则这个函数就是一个生成器的模板
#         a, b = b, a+b
#         current_num += 1
#     return '---ok---'
# 如果在调用gen的时候，发现这个函数中有yield那么此时，不是调用函数，
# 而是创建一个生成器对象

# obj = gen(10)
# 执行obj到yield后会暂停，并将yield后面的对象返回，
# 再次循环时会从yield暂停处继续向下执行


#生成器中的return如果想要捕获，则必须是生成器产生异常的时候，且return的值为
#异常的value属性

# while True:
#     try:
#         ret = next(obj)
#         print(ret)
#     except Exception as e:
#         print(e.value)
#         # 因为是while循环，不加break则会一直打印
#         break


def gen(nums):
    a, b = 0, 1
    current_num = 0
    while current_num < nums:
        ret = yield a     #如果一个函数中有yield语句，则这个函数就是一个生成器的模板
        print('ret:',ret)
        a, b = b, a+b
        current_num += 1

obj = gen(10)

ret = next(obj)
print(ret)

# 可以向生成器传值
# 当运行到yield a时，生成器会停止，将a的值返回给next(obj)
# 当send一个值时，相当于给yield a赋值，也就是yield a = 'hhh'

#send函数也是调用生成器取值，不同的是他可以传值给生成器
ret = obj.send("hhh")


# 了解了next()如何让包含yield的函数执行后，我们再来看另外一个非常重要的函数send(msg)。
# 其实next()和send()在一定意义上作用是相似的，区别是send()可以传递yield表达式的值进去，
# 而next()不能传递特定的值，只能传递None进去。因此，我们可以看做c.next() 和 c.send(None) 作用是一样的。
# 需要提醒的是，第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，否则会出错的，
# 因为没有Python yield语句来接收这个值。
# 原文：https://blog.csdn.net/pfm685757/article/details/49924099

print(ret)


ret = obj.send('bbb')
print(ret)

ret = obj.send('bbb')
print(ret)