# -*- coding: utf-8 -*-
"""
:function: 通过python与selenium将mongoDB中的题目数据自动添加网站中
:author:hefengen
:date:2018/04/14
:email:hefengen@hotmail.com
"""
import time

import pymongo

import re

import requests
from selenium.webdriver.common.keys import Keys
from config import *
from function import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 题目的url
problem_url = 'http://192.168.94.137/admin/problems'

# 创建题目的url
create_problem_url = 'http://192.168.94.137/admin/problem/create'

# login_url
url = 'http://192.168.94.137/admin'

# 使用selenium模拟在浏览器中导入数据
browser = webdriver.Chrome(service_args=SERVICE_ARGS)
wait = WebDriverWait(browser, 10)

# 设置窗口大小
browser.set_window_size(1400, 900)

zip_dir = "E:\\Problem\\Testcase\\ok\\"      # 解压后的目录


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
            EC.presence_of_element_located((By.CSS_SELECTOR, '#app > form > div:nth-child(3) > div > div > input'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > form > div:nth-child(4) > div > button'))
        )
        # 自动填充密码
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        submit.click()

        #clickit = wait.until(
        #    EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div > div:nth-child(1) > ul > li:nth-child(4) > div > i.el-submenu__icon-arrow.el-icon-arrow-down'))
        #)
        #clickit.click()

        #addproblemsbutton = wait.until(
        #    EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div > div:nth-child(1) > ul > li.el-submenu.is-active.is-opened > ul > li.el-menu-item.is-active'))
        #)
        
        #clickita.click()        
        time.sleep(9)

        browser.get('http://192.168.94.137/admin/problems')  
        create_problem = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div > div.content-app > div.view > div.panel > div > div.panel-options > button'))
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
    for problem in data:
        if(problem['sample_input'] != "" and problem['sample_output'] != ""):
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
                time_limit = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(4) > div:nth-child(1) > div > div > div > input'))
                )
                memory_limit = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input'))
                )
                difficulty = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(4) > div:nth-child(3) > div > div > div'))
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
                #hint = wait.until(
                #    EC.presence_of_element_located((By.CSS_SELECTOR,
                #                                    '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(7) > div > div > div.simditor-wrapper > div.markdown-editor > textarea'))
                #)
                file_input = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#app > div > div.content-app > div.problem > div > div > form > div:nth-child(11) > div.el-col.el-col-4 > div > div > div > div > input'))
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
                display_id.send_keys(problem['problem_no'])
                title.send_keys(problem['problem_name'])

                pat = 'src="(.*?)"'
                regex = re.compile(pat, re.S)
                is_description = re.search(pat, problem['description'], re.S)
                if (is_description != None):
                    description_text = regex.sub(lambda m: 'src="/public/' + m.group(1) + '"', problem['description'])
                else:
                    description_text = problem['description']
                description.send_keys(description_text)

                # 输入框
                is_input = re.search(pat, problem['input'], re.S)
                if (is_input != None):
                    # 通过正则表达式替换
                    input_text = regex.sub(lambda m: 'src="/public/' + m.group(1) + '"', problem['input'])
                else:
                    input_text = problem['input']
                input.send_keys(input_text)

                # 输出框
                is_output = re.search(pat, problem['output'], re.S)
                if (is_output != None):
                    output_text = regex.sub(lambda m: 'src="/public/' + m.group(1) + '"', problem['output'])
                else:
                    output_text = problem['output']
                output.send_keys(output_text)

                # 时间、内存、标签、样例
                for i in range(0, 5):
                    time_limit.send_keys(Keys.BACKSPACE)
                time_limit.send_keys('4000')

                memory_limit.clear()
                memory_limit.send_keys(problem['memory_limit'])
                tags.send_keys('bzoj-problem')
                tags.send_keys(Keys.ENTER)
                sample_input.send_keys(problem['sample_input'])
                sample_output.send_keys(problem['sample_output'])

                #is_hint = re.search(pat, problem['hint'], re.S)
                #if (is_hint != None):
                #    hint_text = regex.sub(lambda m: 'src="/public/' + m.group(1) + '"', problem['hint'])
                #else:
                #    hint_text = problem['hint']
                #hint.send_keys(hint_text)
                #time.sleep(5)

                # 点击上传文件
                file_dir = zip_dir + "\\" + problem['problem_no'] + ".zip"
                file_input.send_keys(file_dir)

                source.send_keys(problem['source'])
                time.sleep(5)

                # 提交
                create.click()
            except TimeoutError:
                add_data_to_page()

def main():
    """
    :return:
    """
    handle_login()

if __name__ == '__main__':
    main()

