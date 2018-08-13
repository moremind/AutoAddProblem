# 缘由 

QDUOJ的开发以及众多OJ的题库，使得我们自动化添加题目更加轻松。前提是您需要获得各OJ的测试数据。

# 概况

目前主要模块分为

* 爬虫部分-WebSpider
* 自动化加题部分-AddProblem

因为懒得解析markdown文档，所有用了爬虫scrapy,并且爬虫获取到的数据相对而言文档更容易解析与添加。如果您能够通过pandoc转文件后，将文本提取出来也可以。

# 需要安装的软件

* Python
* MongoDB(V3.4)
* MongoDB 客户端工具-推荐使用RoBo 3T

# 数据（某OJ数据&已经解压完成的）
1000-1999-Testcase数据链接：https://pan.baidu.com/s/1SvCgulQt8rn8m7w0cbMExQ 密码：jg7m

2000-2499-Testcase数据链接：https://pan.baidu.com/s/1tgr1M-VsRrzaEjXPmA3NCA 密码：4mpf

# 题目数据

https://finen-1251602255.cos.ap-shanghai.myqcloud.com/file/bzoj_problem.zip

您可以直接通过MongoDB将将该数据导入到您的Mongo中，导入命令请您自行搜索！

> 如果您对爬虫有兴趣可以参看1.0版本进行对题目数据进行爬取。
https://github.com/hirCodd/AutoAddProblem/blob/master/README_1.0.md

# 图片位置
在本项目中已经提供BZOJ，所以您可以直接在BZOJ解压包中看到JudgeOnline找到upload以及images两个图片目录，你只需要将这个两个目录复制到已经部署好的qduoj的public目录下即可。
![dir][2]

# 安装自动加题所需要的库
1. webdriver
2. selenium
3. pymongo

* 执行自动加题
> 也需要修改您的url以及mongoDB配置，以及OJ的管理员的用户名、密码。

1. url在add_problem.py
2. MongoDB配置在settings.py
3. OJ用户名以及密码在config.py
4. 修改zip_dir = "E:\\Problem\\Testcase\\ok"为您重新压缩后的目录。

* 执行：python add_problem.py


# 某些bug
* 因为BZOJ数据问题，可能导致添加题目突然中止，你可能需要执行删除数据库文档的命令，然后重新执行：python add_problem.py即可再次添加题目。
> 在delete.py中，你需要修改count的值以及for循环的值，删除已经添加得文档。示例如下：

    # 删除编号自1200开始，至1245的所有文档数据
    for i in range(0, 46):
        count = 1200
        count = count+i
        print(count)
        db.problem.delete_one({"problem_no": str(count)})


![oj][1]

  [1]: https://s1.ax2x.com/2018/06/02/71uIJ.png
  [2]: https://finen-1251602255.cos.ap-shanghai.myqcloud.com/images/github/autoaddproblem/dir.png