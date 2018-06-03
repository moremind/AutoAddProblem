from function import *
from pymongo import *

def delete():
    try:
        # 创建连接对象
        client = MongoClient(host="localhost", port=27017)

        db = client.bzoj

        # 删除编号自1200开始，至1245的所有文档数据
        for i in range(0, 46):
            count = 1200
            count = count+i
            print(count)
            db.problem.delete_one({"problem_no": str(count)})
            # 所有符合条件数据都删除
            print("删除成功")

    except Exception as e:
        print(e)

if __name__ == '__main__':
    delete()
