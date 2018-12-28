## 缘由 

QDUOJ的开发以及众多OJ的题库，使得我们自动化添加题目更加轻松。前提是您需要获得各OJ的测试数据。**请注意本方法只用在您的机器上运行即可，不用再OJ服务器运行！**

## 概况

目前主要模块分为

* 爬虫部分-WebSpider
* 自动化加题部分-AddProblem

用了爬虫scrapy,并且爬虫获取到的数据相对而言文档更容易解析与添加。如果您能够通过pandoc转文件后，将文本提取出来也可以。

## 需要安装的软件

* Python3.6
* MongoDB(V3.4)
* MongoDB 客户端工具-推荐使用RoBo 3T

Mongo安装教程：[mongo安装](https://blog.csdn.net/heshushun/article/details/77776706)（教程源于-李子园的梦想）


## 数据（某OJ数据&已经解压完成的）
1000-1999-Testcase数据链接：https://pan.baidu.com/s/1SvCgulQt8rn8m7w0cbMExQ 密码：jg7m

2000-2499-Testcase数据链接：https://pan.baidu.com/s/1tgr1M-VsRrzaEjXPmA3NCA 密码：4mpf

2500-2999-Testcase数据链接：https://pan.baidu.com/s/1X3HVJTGCFhHo-p6R_G0sSw 密码：scgq

3000-3499-Testcase数据链接：https://pan.baidu.com/s/1KjosY3Sr7XbSqbZo4Cdfkg 密码：rdr4

3500-3999-Testcase数据链接：https://pan.baidu.com/s/16eJWeheUgKJeuQDGVSKHuw 密码：goii

4000-4499-Testcase数据连接：https://pan.baidu.com/s/1Yt-MZHvDPGtQooUgt9yJ1Q 密码：1pu0

4500-4999-Testcase数据连接：https://pan.baidu.com/s/1Dz9bDHzkpsx9jOxHSp2IeQ 密码：tv9g

## 题目数据

https://finen-1251602255.cos.ap-shanghai.myqcloud.com/file/bzoj_problem.zip

您可以直接通过MongoDB将将该数据导入到您的Mongo中。
导入命令如下：
```
linux下可以使用：mongorestore -d <db_name> <bson_folder>
windows下可以使用：mongorestore.exe -d <db_name> <bson_folder>

windows下： mongorestore.exe -d bzoj D:\Mongo\bin\dump\bzoj_problem\problem.bson
linux下： mongorestore -d bzoj /usr/DB/bzoj_problem/problem.bson
```

> 如果您对爬虫有兴趣可以参看1.0版本进行对题目数据进行爬取。
https://github.com/hirCodd/AutoAddProblem/blob/master/README_1.0.md

## 图片位置
在本项目中已经提供BZOJ，所以您可以直接在BZOJ解压包中看到JudgeOnline找到upload以及images两个图片目录，你只需要将这个两个目录复制到已经部署好的qduoj的public目录下即可。
![dir][2]

## 安装自动加题所需要的库
1. webdriver
2. selenium
3. pymongo

安装方法：
```
pip install selenium
pip install pymongo
```

webdriver下载地址：[chromedriver](https://finen-1251602255.cos.ap-shanghai.myqcloud.com/file/chromedriver.exe)
webdriver放置位置如下：

![webdriver][4]


* 执行自动加题
> 也需要修改您的url以及mongoDB配置，以及OJ的管理员的用户名、密码。

1. url在add_problem.py
2. MongoDB配置在settings.py
3. OJ用户名以及密码在config.py
4. 修改zip_dir = "E:\\Problem\\Testcase\\ok"为您重新压缩后的目录。

* 执行：python add_problem.py


## 某些bug
* 因为BZOJ数据问题，可能导致添加题目突然中止，你可能需要执行删除数据库文档的命令，然后重新执行：python add_problem.py即可再次添加题目。
> 在delete.py中，你需要修改count的值以及for循环的值，删除已经添加得文档。示例如下：

    # 删除编号自1200开始，至1245的所有文档数据
    for i in range(0, 46):
        count = 1200
        count = count+i
        print(count)
        db.problem.delete_one({"problem_no": str(count)})


![oj][1]
![oj1][3]


  [1]: https://s1.ax2x.com/2018/06/02/71uIJ.png
  [2]: https://finen-1251602255.cos.ap-shanghai.myqcloud.com/images/github/autoaddproblem/dir.png
  [3]: https://finen-1251602255.cos.ap-shanghai.myqcloud.com/images/github/autoaddproblem/p.png
  [4]: https://finen-1251602255.cos.ap-shanghai.myqcloud.com/images/github/autoaddproblem/webdriver.png