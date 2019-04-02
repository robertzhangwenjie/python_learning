# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/4/2 9:52
# File  :  request_resolver.py
# IDE   :  PyCharm

import re

# 解析请求的第一行
def get_request_data(request):
    request_dict = {}
    request_value = re.match(r'([^/]+)\s(/.*)\s(.*)',request)
    request_dict['method'] = request_value.group(1)
    print(request_dict['method'])
    request_dict['uri'] = request_value.group(2)
    print(request_dict['uri'])
    request_dict['http_version'] = request_value.group(3)
    print(request_dict['http_version'])
    # print(request_value.group(1))
    return request_dict


if __name__ == '__main__':

    request = 'GET / HTTP/1.1'
    print(get_request_data(request))