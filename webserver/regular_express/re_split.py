# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/4/1 8:20
# File  :  re_split.py
# IDE   :  PyCharm

import re

s = 'zhang,wenjie robert'
# 根据匹配到的字符串进行切割
v = re.split(r'[:, ]',s)
print(v)
