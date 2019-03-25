# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/19 15:54
# File  :  base64_encode.py
# IDE   :  PyCharm

import base64

def base64_encode(password):
    return base64.b64encode(password.encode('utf-8'))


if __name__ == '__main__':
    print(str(base64_encode('888888'),'utf-8'))