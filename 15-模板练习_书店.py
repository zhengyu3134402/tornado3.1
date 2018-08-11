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

# 定义了Application子类， 定义__init__方法
class Application(tornado.web.Application):

    def __init__(self):

        # 创建了处理类列表
        handlers = [

            (r"/", Main_handler),
        ]

        # 设置了一个字典
        settings = dict(

            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            # 关闭自动转义
            autoescape=None,
            # 关闭转义的另一种方法是在模板中 {% autoescape None %}
            # 关闭转义单个内容在模板中用 {% raw xxxx %}
        )

        # 在初始化子类的调用中传递这些值
        tornado.web.Application.__init__(self, handlers, **settings)

class Main_handler(tornado.web.RequestHandler):

    def get(self):
        self.render(
            'main15_son.html',
            page_title="Burt's Books | Home",
            header_text="Welcome to Burt's Books!",
        )



if __name__ == '__main__':

    tornado.options.parse_command_line()

    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()