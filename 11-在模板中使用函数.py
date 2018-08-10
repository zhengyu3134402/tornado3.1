# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

define('port', default=8000, type=int, help='端口')

class Index_handler(tornado.web.RequestHandler):

    def get(self):

        # autocaping=None 关闭了自动转义
        self.render('temp_func.html', a='& < >', b='http://www.baidu.com?a=哈哈',
                    c={'c1': 'c2'}, d='1    2    3  4     6', autoscaping=None, e='& < >')

if __name__ == '__main__':

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[

        (r"/", Index_handler),
    ], template_path=os.path.join(os.path.dirname(__file__), "templates"))
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
