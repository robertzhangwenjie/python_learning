# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/26 15:14
# File  :  reg_demo.py
# IDE   :  PyCharm

import re

# s = 'joinhubjoin'
# 如果有返回值则匹配成功，返回空则匹配失败
# 默认从头开始匹配，不判断结尾，且只匹配第一个
# res = re.match(r'join.',s)

# 提取出满足规范的值
# 如果res匹配为空，则会报错
# print(res.group())


# 匹配[a-bc-z] 代表匹配a-b和c-z中的一个d
# [1-38-9] 匹配1-3 8-9
# [1-8abcd] 匹配1-8 abcd
# res = re.match(r'join[a-bc-z]',s)
# print(res.group())

# . 匹配任意单个字符，除了\n
# s = 'joinsen\n覆盖到'
# print(re.match(r'joinse.*',s).group())
# 匹配结果: joinsen 匹配不到\n

# \w 匹配[0-9a-zA-Z_] 也匹配其他语言(如中文等)
# \W 匹配单个非单词字符

# \s匹配单个空白字符 如tab建和空格
# s = 'join se'
# print(re.match(r'join\s[a-z]',s).group())
# 匹配结果: join s

#  \S匹配单个非空白字符
# s = 'joinse'
# print(re.match(r'join\S',s).group())
# 匹配结果: joins


# {m} {m,n} 匹配多个

# * 匹配0或者任意多个

# re.S
# 如果不使用re.S参数，则只在每一行内进行匹配，
# 如果一行没有，就换下一行重新开始，不会跨行。
# 而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，
# 将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配
s = 'joinsen\n覆盖到'
print(re.match(r'.*',s,re.S).group())
# 匹配结果:joinsen
#           覆盖到

# ...$判断以...结尾

# 匹配邮箱地址
# 要求: @符号之前有4到20位
def is_email(email):
    res = re.match(r'^[1-9a-zA-Z_]{4,20}@[1-9a-z]+\.com$',email)
    if res:
        print('匹配成功:',res.group())
    else:
        print('不符合邮箱要求:',email)

if __name__ == '__main__':
    is_email('_1648855816@qq.com')



