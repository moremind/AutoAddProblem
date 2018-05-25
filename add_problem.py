# -*- coding: utf-8 -*-
"""
:function: 通过python与selenium将mongoDB中的题目数据自动添加网站中
:author:hefengen
:date:2018/04/14
:email:hefengen@hotmail.com
"""
import time
import pymongo
import requests
from selenium.webdriver.common.keys import Keys

from config import *
from settings import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pack_sample import *


# 题目的url
problem_url = 'http://www.yiwailian.cn/admin/problems'

# 创建题目的url
create_problem_url = 'http://www.yiwailian.cn/admin/problem/create'

# login_url
url = '***'

# 使用selenium模拟在浏览器中导入数据
browser = webdriver.Chrome(service_args=SERVICE_ARGS)
wait = WebDriverWait(browser, 10)

# 设置窗口大小
browser.set_window_size(1400, 900)

# session设置
session = requests.Session()


def handle_login():
    """
    :function: 模拟实现登陆
    :return:
    """
    try:
        browser.get(url=url)
        username = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#app > form > div:nth-child(2) > div > div.el-input > input'))
        )
        password = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#app > form > div:nth-child(3) > div > div.el-input > input'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > form > div:nth-child(4) > div > button'))
        )
        # 自动填充密码
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        submit.click()

        create_problem = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.view > div.panel > div > div.panel-options > button > span'))
        )
        create_problem.click()
        add_data_to_page()
    except TimeoutError:
        handle_login()

def add_data_to_page():
    """
    :param url:
    :return:
    """
    data = query_data_from_mongo()
    try:
        browser.get(create_problem_url)
        display_id = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(1) > div.el-col.el-col-6 > div > div > div.el-input > input'))
        )
        title = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(1) > div.el-col.el-col-18 > div > div > div.el-input > input'))
        )
        description = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(2) > div > div > div > div > div.simditor-wrapper > div.markdown-editor > textarea'))
        )
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(3) > div:nth-child(1) > div > div > div > div.simditor-wrapper > div.markdown-editor > textarea'))
        )
        output = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(3) > div:nth-child(2) > div > div > div > div.simditor-wrapper > div.markdown-editor > textarea'))
        )
        tag = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(5) > div:nth-child(2) > div > div > button > span'))
        )
        tag.click()
        tags = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(5) > div:nth-child(2) > div > div > div > div.el-input.el-input--mini > input'))
        )
        sample_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(6) > div > div > div > div > div > div:nth-child(1) > div > div > div > textarea'))
        )
        sample_output = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(6) > div > div > div > div > div > div:nth-child(2) > div > div > div > textarea'))
        )
        file_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(10) > div.el-col.el-col-4 > div > div > div > div > input'))
        )
        source = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(12) > div > div > input'))
        )
        create = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                '#app > div > div.content-app > div.problem > div > div > form > button'))
        )
        # 发送相关的信息

        # TODO 2018/04/16 循环获取数据并且对ID赋值
        display_id.send_keys('5')
        title.send_keys(data['problem_name'])
        description.send_keys(data['description'])
        input.send_keys(data['input'])
        output.send_keys(data['output'])
        tags.send_keys('nyist_problem')
        tags.send_keys(Keys.ENTER)
        sample_input.send_keys(data['sample_input'])
        sample_output.send_keys(data['sample_output'])

        # 点击上传文件
        file_dir = pack_data(problem_name=data['problem_name'], sample_input=data['sample_input'],
                             sample_output=data['sample_output'])
        # FIXME 测试用例的bug
        file_input.send_keys(file_dir)
        time.sleep(5)
        source.send_keys('nyist_oj_problem')

        # 提交
        create.click()
        time.sleep(10)

    except TimeoutError:
        add_data_to_page()

def main():
    """
    :return:
    """
    handle_login()
    # query_data_from_mongo()

if __name__ == '__main__':
    main()

