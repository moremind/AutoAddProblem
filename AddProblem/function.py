# -*- coding: utf-8 -*-
"""
:function: mongoDB数据库连接函数
:author:hefengen
:date:2018/04/15
:email:hefengen@hotmail.com
"""

from settings import *
import pymongo

def get_collection():
    """
    :function: 连接数据库
    :return: collection
    """
    client = pymongo.MongoClient(MONGO_URI)
    db = client[MONGO_DATABASE]
    collection = db[MONGO_TABLE]
    return collection

def query_data_from_mongo():
    """
    :function:从mongoDB中取数据
    :return:
    """
    collection = get_collection()
    query_filter = collection.find().sort("problem_no")
    # query_filter = collection.find_one({"problem_no": "1019"})
    return query_filter
