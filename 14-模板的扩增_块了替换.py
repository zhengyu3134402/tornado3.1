# -*- coding:utf-8 -*-

import sys
import os
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
reload(sys)
sys.setdefaultencoding('utf-8')

define('port', default=8000, type=int, help='端口')
class Index_handler(tornado.web.RequestHandler):

    def get(self):

        a = '变量a的值'
        self.render('main_son.html', a=a)

if __name__ == '__main__':

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/', Index_handler),
    ], template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()