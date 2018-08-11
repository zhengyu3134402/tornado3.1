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

class Hello_handler(tornado.web.RequestHandler):

    def get(self):
        self.render('hello16.html')

class Hello_module(tornado.web.UIModule):

    # 返回填充的字符串
    def render(self):
        return '<h1>Hello, world!</h1>'

if __name__ == '__main__':

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/', Hello_handler),
    ], template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True,
        # 把名为Hello的模块的引用和我们定义的Hello_module类结合了起来
        # 当调用Hello_handler并渲染hello.html时候，可以用{% module Hello() %}
        # 模板标签来包含Hello_module类中render方法返回的字符串
        ui_modules={'Hello': Hello_module})
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()