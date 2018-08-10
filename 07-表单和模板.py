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
        # 一旦告诉tornado在哪里找到模板，我们可以使用RequestHandler类的render方法来告诉tornado读入
        # 读入模板文件,插入其中模板的代码，并返回结果给浏览器
        # 这段代码的意识是 告诉tornado在templates目录中找到一个名为index.html的文件，读取其中的
        # 内容， 并且发送给浏览器
        self.render('index.html')

class Testpost_handler(tornado.web.RequestHandler):

    def post(self):

        # 告诉模板使用变量noun1作为模板中roads的值
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

        # 向Application对象的__init__方法传递了一个template_path 参数
        # template_path参数告诉tornado在哪里找模板，在tornado应用文件的同目录下
        # templates文件夹中寻找模板
    ], template_path=os.path.join(os.path.dirname(__file__), "templates"))
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
