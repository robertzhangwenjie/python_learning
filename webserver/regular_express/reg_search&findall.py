# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/26 17:13
# File  :  reg_search&findall.py
# IDE   :  PyCharm
import re

s = 'eabc...abc'

# 默认从第一个字符开始匹配第一个符合规则的字符串
print(re.match(r'abc',s))

# 全局匹配第一个符合规则的
print(re.search(r'abc',s).group())

# 匹配所有符合规则的，并返回一个list
print(re.findall(r'abc',s))

# 匹配到后进行全局替换
print(re.sub(r'abc','def',s))
