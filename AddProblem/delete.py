from function import *
from pymongo import *

def delete():
    try:
        # 1 创建连接对象
        client = MongoClient(host="localhost", port=27017)

        db = client.bzoj    # 使用demo数据库
        # 修改数据
        # 修改第一条符合条件的文档删除
        for i in range(0, 101):
            count = 1101
            count = count+i
            print(count)
            db.problem.delete_one({"problem_no": str(count)})  # 把年龄是18的第一条文档删除
            # 所有符合条件数据都删除
            print("删除成功")

    except Exception as e:
        print(e)

if __name__ == '__main__':
    delete()
