# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/3/21 8:55
# File  :  copy.py
# IDE   :  PyCharm

'''
实现多进程拷贝文件夹
'''


import os
import multiprocessing
import sys
import shutil


if len(sys.argv) != 3:
    print('useage: %s file1 file2'%sys.argv[0])
    exit(1)
copy_file_name = sys.argv[1]
dest_file_name = sys.argv[2]


# 创建一个拷贝函数copy_file
def _copy_file(src_file, dest_file):
    print('starting copy file:%s to %s' % (src_file, dest_file))

    # 判断复制的文件是否为文件夹，如果为文件夹则递归调用复制函数
    if os.path.isdir(src_file):
        os.mkdir(dest_file)
        files = os.listdir(src_file)
        for file in files:
            s_file = src_file + '/' + file
            d_file = dest_file + '/' + file
            _copy_file(s_file, d_file)
    try:
        f_read = open(src_file, 'rb')
        f_write = open(dest_file, 'wb')

        while True:
            # 防止文件过大时占用内存，设置一个缓存size为1024kb
            content = f_read.read(1024)
            if content:
                f_write.write(content)
            else:
                break
            f_write.close()
            f_read.close()
            print('copy %s to %s success' % (src_file, dest_file))
    except Exception as e:
        print('复制失败:%s'%e)

def copy(copy_folder_name,dest_folder_name):
    # # 1.获取需要拷贝的文件夹
    # copy_folder_name = input("please input your want copy file:")
    #
    # # 2.获取目标文件夹
    # dest_folder_name = input("please input your dest folder name:")

    if os.path.exists(dest_folder_name):
        confirm_value = input("%s already exist,whether to cover it {yes|no}:" % dest_folder_name)
        if confirm_value == 'yes' or 'y':
            # 递归删除整个文件夹
            shutil.rmtree(dest_folder_name)
            os.mkdir(dest_folder_name)
        else:
            exit(1)
    # 3.获取拷贝文件夹下所有的文件名
    copy_files = os.listdir(copy_folder_name)
    print(copy_files)


    # 5.创建一个进程池，用于多进程处理
    po = multiprocessing.Pool(multiprocessing.cpu_count())

    # 6.创建一个队列用于子进程和主进程进行通信
    qu = multiprocessing.Manager().Queue()

    # 7.向进程中添加任务
    for file in copy_files:
        src_file = copy_folder_name + '/' + file
        dest_file = dest_folder_name + '/' + file
        # 加入target到进程池中
        po.apply_async(_copy_file, args=(src_file, dest_file))
    po.close()
    po.join()
    print('copy end')


copy(copy_file_name,dest_file_name)

if __name__ == '__main__':
    pass
