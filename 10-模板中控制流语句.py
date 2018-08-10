# -*- coding:utf-8 -*-

import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

define('port', default=8000, type=int, help='端口')

class Index_handler(tornado.web.RequestHandler):

    def get(self):

        a = self.get_argument('a', 'hhhhh')

        self.write(a +' goodmorning')

class Book_handler(tornado.web.RequestHandler):

    def get(self):

        self.render('book.html', title='Home page', header="书BOOKS",
                    books=["书名1", "书名2", "书名3"])

if __name__ == '__main__':

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[


        (r"/", Index_handler),
        (r"/book", Book_handler),
    ], template_path=os.path.join(os.path.dirname(__file__), "templates"))
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
