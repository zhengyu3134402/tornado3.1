# -*- coding:utf-8 -*-

import sys
import os.path
reload(sys)
sys.setdefaultencoding('utf-8')
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

define('port', default=8000, type=int, help='端口')

class Index_handler(tornado.web.RequestHandler):

    def get(self):

        # 渲染模板
        self.render('index.html')

class Testpost_handler(tornado.web.RequestHandler):

    def post(self):

        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('testpost.html', roads=noun1, wood=noun2, made=verb,
                    difference=noun3)


if __name__ == '__main__':

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[


        (r"/", Index_handler),
        (r"/testpost", Testpost_handler),
    ], template_path=os.path.join(os.path.dirname(__file__), "templates"))
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
