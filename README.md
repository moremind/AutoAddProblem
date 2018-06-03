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

# 准备
* 解压获取已准备好的BZOJ
你需要将BZOJ目录下的压缩文件解压，解压至你的web服务器目录下。


* 安装scrapy
具体安装文档请见docs。


* 启动爬虫并检查数据库是否存在数据
* 1. 修改爬虫配置:

 url在bzoj.py
 MongoDB数据配置在settings.py


* 2.执行爬虫：scrapy crawl bzoj

* 执行自动加题
> 也需要修改您的url以及mongoDB配置，以及OJ的用户名、密码。

1. url在add_problem.py
2. MongoDB配置在settings.py
3. OJ用户名以及密码在config.py

执行：python add_problem.py

# 图片位置
在本项目中已经提供BZOJ，所以您可以直接在BZOJ解压包中看到JudgeOnline找到upload以及images两个图片目录，你只需要将这个两个目录复制到已经部署好的qduoj的 public目录下。
![dir][2]

# 某些bug
* 因为BZOJ数据的问题，某一题如果有两张或者以上的图片，则可能显示不全。
* 因为BZOJ数据问题，可能导致添加题目突然中止，你可能需要执行删除数据库文档的命令
> 在delete.py中，你需要修改count的值以及for循环的值，删除已经添加得文档。然后重新执行：python add_problem.py即可再次添加题目。

![oj][1]


  [1]: https://s1.ax2x.com/2018/06/02/71uIJ.png
  [2]: https://finen-1251602255.cos.ap-shanghai.myqcloud.com/images/github/autoaddproblem/dir.png