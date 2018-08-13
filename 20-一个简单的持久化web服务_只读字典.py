# -*- coding:utf-8 -*-
'''
# 目的：发送一个单词请求，返回这个单词的定义

# 向数据库中添加一些单词
# 导入了模块
from pymongo import MongoClient

# 创建连接对象
client = MongoClient('localhost', 27017)

# 创建了新的数据库
db = client['word']

# 像集合中添加信息
db.word.insert({'word': 'a', 'definition': 'A'})
db.word.insert({'word': 'b', 'definition': 'B'})
db.word.insert({'word': 'c', 'definition': 'C'})
'''
import sys
import os
import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
from tornado.options import define, options
reload(sys)
sys.setdefaultencoding('utf-8')
from pymongo import MongoClient

define('port', default=8000, type=int, help='端口')

class Word_handler(tornado.web.RequestHandler):

    def get(self, word_t):

        # 一旦在Application对象中添加了db属性，就可以在任何RequestHandler对象中使用
        # self.application.db 访问它，这正式我们为了取出pymongo的word集合兑现在Word_handler
        # 中get方法所做的事情
        # 将集合变量指定给coll
        coll = self.application.db.word

        word_doc = coll.find_one({'word': word_t})

        # 如果发现这个单词，从该文档的字典中删除_id键（以便python的json库可以将其序列化）
        # 然后将其传递给RequestHandler的write方法，write方法会自动序列化字典为JSON格式
        if word_doc:
            del word_doc["_id"]
            self.write(word_doc)

        # 如果find_one方法没有匹配到任何对象，则返回None
        else:
            # 响应状态设置为404
            self.set_status(404)
            # 写一个简短的json来提示用户这个单词在数据库中没有找到
            self.write({'error': 'word not found'})




class Application(tornado.web.Application):

    def __init__(self):

        handlers = [(r'/(\w+)', Word_handler)]

        # 在tornado Application对象的__init__方法中实例化了一个pymongo连接对象
        coon = MongoClient('localhost', 27017)

        # 创建了db属性 指向了mongodb的word数据库
        self.db = coon['word']

        tornado.web.Application.__init__(self, handlers, debug=True)

if __name__ == '__main__':

    tornado.options.parse_command_line()



    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()