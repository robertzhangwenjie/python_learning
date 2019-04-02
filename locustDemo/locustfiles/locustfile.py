# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/1/14 12:42
# File  :  locustfile.py
# IDE   :  PyCharm
import sys,os
sys.path.append(os.getcwd())

from locust import HttpLocust,TaskSet,task

class MyTaskSet(TaskSet):
    @task
    def my_task(self):
        self.client.get("/")

    def stop(self):
        self.interrupt()

class MyLocust(HttpLocust):
    host = 'http_demo://www.ovupark.com'
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 3000

