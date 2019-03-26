# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/26 9:03
# File  :  gevent_practice.py
# IDE   :  PyCharm
import pprint
import time


import gevent
from gevent import monkey
monkey.patch_all()

import random
import requests
def downloader(url):
    # url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2349141039,2261551338&fm=26&gp=0.jpg'
    res = requests.get(url)
    img_content = res.content
    count_number = random.randint(1,10)
    save_file = "%s.jpg"%count_number
    with open(save_file,'wb') as f:
        f.write(img_content)
    time.sleep(0.5)

def main():


    url1 = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2349141039,2261551338&fm=26&gp=0.jpg'
    url2 = 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=336419783,3084030113&fm=26&gp=0.jpg'
    gevent.joinall([
        gevent.spawn(downloader,url1),
        gevent.spawn(downloader,url2)
    ])

if __name__ == '__main__':

    main()


