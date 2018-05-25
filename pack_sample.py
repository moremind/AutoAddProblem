# -*- coding: utf-8 -*-
"""
:function: 通过python将mongoDB的sample做成文件并且打包并且选择文件
:author:hefengen
:date:2018/04/15
:email:hefengen@hotmail.com
"""

from function import *
import os, zipfile

def make_dir():
    """
    :function: 使用题目名称生成一个文件夹
    :return: 当前生成的最新目录
    """
    directory = os.getcwd()
    data = query_data_from_mongo()

    cur_dir = ''
    for k, v in enumerate(data['problem_name']):
        cur_dir = directory + "\\" + v + "\\"

    # 判断是否存在
    if not os.path.exists(cur_dir):
        os.mkdir(cur_dir)
    else:
        print('Already Exist')
    return cur_dir

def pack_data(problem_name, sample_input, sample_output):
    """
    :function: 从mongo中选择数据并且将data打包成一个zip
    :return: 打包后的文件路径
    """

    filename = ''
    for k, v in enumerate(problem_name):
        filename = str(v)

    # get dir
    cur_dir = make_dir()

    file_in_dir = cur_dir+"1.in"
    fi = open(file_in_dir, 'w')
    for k, v in enumerate(sample_input):
        fi.write(str(v))
    fi.close()

    file_out_dir = cur_dir + "1.out"
    fo = open(file_out_dir, 'w')
    for k, v in enumerate(sample_output):
        fo.write(str(v))
    fo.close()

    # 对当前生成的文件打包压缩
    file_dir = zip_compress(cur_dir=cur_dir, filename=filename)

    return file_dir

def zip_compress(cur_dir, filename):
    """
    :function: 将目录下的文件打包成zip格式文件
    :param cur_dir: 当前cur_dir
    :param filename:文件名称
    :return: zip的文件路径
    """

    # 通过目录对文件打包
    new_file = cur_dir + filename + ".zip"
    file = zipfile.ZipFile(new_file, 'w', zipfile.ZIP_DEFLATED)

    # TODO 2018/04/16 修改只选择当前的目录解决压缩两次的bug
    for dirpath, dirname, filenames in os.walk(cur_dir):
        fpath = dirpath.replace(cur_dir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            file.write(os.path.join(dirpath, filename), fpath+filename)
    file.close()
    return new_file


# if __name__ == '__main__':
#     data = query_data_from_mongo()
#     problem_name = data['problem_name']
#     sample_input = data['sample_input']
#     sample_output = data['sample_output']
#     print(problem_name)
#     file_dir = pack_data(problem_name=problem_name, sample_input=sample_input, sample_output=sample_output)
#     print(file_dir)

