# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2018/12/10 17:14
# File  :  testlinkDemo.py
# IDE   :  PyCharm


from testlink import *


TESTLINK_API_PYTHON_SERVER_URL = "http_demo://http_demo://47.104.107.48:8088/testlink/lib/api/xmlrpc.php"
TESTLINK_API_PYTHON_DEVKEY = ["d0bf6c729756c421d6f02e4fab1b2088"]
tls = TestlinkAPIClient(TESTLINK_API_PYTHON_SERVER_URL,TESTLINK_API_PYTHON_DEVKEY)
print(tls.about())