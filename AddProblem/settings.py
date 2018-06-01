"""
:function: MongoDB配置以及其他配置
:author:hefengen
:date:2018/04/15
:email:hefengen@hotmail.com
"""

# request headers
Headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.yiwailian.cn',
    'If-Modified-Since': 'Sat, 24 Feb 2018 13:17:46 GMT',
    'If-None-Match': 'W/"5a9165fa-2f2"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

# MongoDB配置
MONGO_URI = 'localhost'
MONGO_DATABASE = 'bzoj'
MONGO_TABLE = 'problem'

# Service_Agrs配置
SERVICE_ARGS = ['--load-images=true', '--disk-cache=true']