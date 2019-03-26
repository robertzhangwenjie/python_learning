# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/26 16:20
# File  :  reg_grouping.py
# IDE   :  PyCharm

import re
# 匹配邮箱地址
# 要求: @符号之前有4到20位,并打印出其服务器

# ()表示分组提取，group(n)用来提取低n个分组 group() 其实是group(0)
def is_email(email):
    res = re.match(r'^([1-9a-zA-Z_]){4,20}@([1-9a-z]+)\.com$',email)
    if res:
        print('匹配成功:',res.group())
        if res.group(2):
            print('邮箱服务器:',res.group(2))
    else:
        print('不符合邮箱要求:',email)


# 案例2 要求判断一段html标签是否书写正确
# 列如 <h1></h1>

def is_html(html_str):
    # 分组调用，当前面有分组()后，表达式后面可以用\n来引用第几组分组
    res = re.match(r"^<([0-9a-z]+)>.*</\1>$",html_str)
    if res:
        print('是html标签:',html_str)
    else:
        print('不是html标签:',html_str)

html_str = '<body><001>我是</001></body>'
is_html(html_str)


# 分组取别名 (?P<name>xxx)             在django中url匹配时经常用到
# 引用分组别名  (?P=name)
res = re.match(r"^<(?P<name>[0-9a-z]+)>.*</(?P=name)>$", html_str)

