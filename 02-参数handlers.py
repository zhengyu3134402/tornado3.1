# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import tornado.options
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

define('port', default=8000, type=int, help='端口')

class Index_handler(tornado.web.RequestHandler):

    def get(self):

        a = self.get_argument('arga', 'hahaha')
        self.write(a + ' friend!!')

if __name__ == "__main__":

    tornado.options.parse_command_line()

    # handlers 他是一个元祖组成的列表，其中每个元祖的第一个元素是一个用于匹配的正则表达式
    # 第二个元素是一个RequestHandler类，
    app = tornado.web.Application(handlers=[

        (r"/", Index_handler),
    ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()