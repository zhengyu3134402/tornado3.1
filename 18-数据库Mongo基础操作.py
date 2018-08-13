# -*- coding:utf-8 -*-

# mongodb与python做 API互动需要安装pymongo模块

# 安装方法 python -m pip install pymongo


# 创建连接

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
# 或者使用MongoDB URI格式
# client = MongoClient('mongodb://localhost:27017')

# 获取数据库
# 变量 = MongoClient对象中的数据
db = client['sub']   # 或者client.stu

# 获取数据库中的列表(集合)
print(db.collection_names())

# 向集合中添加数据(文档)
    # 变量 = 数据库.集合名
posts = db.posts

    # 集合名.insert_one({数据})
post_id = posts.insert_one({'e': 'k'})

print(post_id)
# 获取集合中文档的一条数据
print(posts.find_one({'e': 'k'}))

# 修改文档中数据 记住要保存save
a = posts.find_one({'e': 'k'})
a['e'] = 'dddd'
db.posts.save(a)
print (a)

# 获取所有文档并用for迭代打印
for i in posts.find():
    print(i)

# 删除文档
posts.remove({'e': 'k'})


