# -*- coding:utf-8 -*-

# PyMongo 从MongoDB中取出的文档是一个简单的字典，不能直接使用json模块的dumps()函数
# 将其转化为JSON，因为json模块不知如何转行MongoDB的objectID类型到JSON，最简单解决次方法
# 将将得到的数据主键删除

from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)

db = client['sub']

# print(db.collection_names())

data = db['posts']

a = data.find_one({'e': 'dddd'})

del a['_id']   # 删除_id键

json.dumps(a)  # 转换诶JSON格式

print(a)