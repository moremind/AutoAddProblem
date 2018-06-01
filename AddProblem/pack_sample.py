# -*- coding: utf-8 -*-
"""
:function: 通过MongoDB进行配置选择zip文件解压与重新压缩
:author:hefengen
:date:2018/04/15
:email:hefengen@hotmail.com
"""

from function import *
import os, zipfile

start_dir = "E:\\Problem\\Testcase\\no"    # 需要遍历的目录
zip_dir = "E:\\Problem\\Testcase\\ok"      # 解压后的目录


def unzip():
    """
    :function: 解压文件
    :return:
    """
    # 从mongodb中获取数据
    data = query_data_from_mongo()
    # 根据数据进行解压
    for problem in data:
        problem_no = problem['problem_no']
        file_name = start_dir + "\\" + problem_no + ".zip"
        if (os.path.exists(file_name)):
            zip_file = zipfile.ZipFile(file_name)
            zip_file.extractall(zip_dir)
        else:
            print(file_name + "Not Exist")

def zip_compress():
    """
    :function: 对指定目录下的文件进行压缩
    :return:
    """

    data = query_data_from_mongo()
    for problem in data:
        problem_no = problem['problem_no']
        new_dir = zip_dir + "\\" + problem_no
        new_file = new_dir + ".zip"
        zip_file = zipfile.ZipFile(new_file, 'w', zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(new_dir, topdown=False):
            fpath = dirpath.replace(new_dir, '')
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                zip_file.write(os.path.join(dirpath, filename), fpath + filename)
        zip_file.close()


if __name__ == '__main__':

    unzip()

    # 开启多线程压缩文件
    zip_compress()


