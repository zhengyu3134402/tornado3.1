# -*- coding:utf-8 -*-

import os
import sys
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
from pymongo import MongoClient
reload(sys)
sys.setdefaultencoding('utf-8')

define('port', default=8000, type=int, help='port')

class Word_handler(tornado.web.RequestHandler):

    def get(self, word_t):

        coll = self.application.db.word

        word_doc = coll.fine_one({"word": word_t})

        if word_doc:

            del word_doc['_id']
            self.write(word_doc)

    def post(self, word):

        # 使用get_argument方法取得POST请求中传递的definition参数
        definition = self.get_argument('definition')

        # 连接数据库并指向集合word
        coll = self.application.db.word

        # 在集合word中查找完那当
        word_doc = coll.fine_one({'word': word})

        # 如果查到
        if word_doc:

            # 将里面的键改成get_argument方法获取的参数
            word['definition'] = definition

            # 保存更改
            coll.save(word_doc)

        else:

            # 如果没找到

            word_doc = {"word": word, 'definition': definition}

            # 向该集合中添加文档word_doc
            coll.insert(word_doc)

        # 删除id主键
        del word_doc['_id']

        self.write(word_doc)




class Application(tornado.web.Application):

    def __init__(self):

        handlers = [

            (r'/(\w+)', Word_handler),
        ]

        client = MongoClient('localhost', 27017)

        self.db = client['word']

        tornado.web.Application.__init__(self, handlers=handlers,
                                         debug=True)

if __name__ == '__main__':

    tornado.options.parse_command_line()

    http_server = tornado.httpserver.HTTPServer(Application())

    http_server.listen(options.port)

    tornado.ioloop.IOLoop.instance().start()
