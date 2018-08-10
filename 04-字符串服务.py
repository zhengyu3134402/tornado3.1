# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import tornado.web
import tornado.options
import tornado.ioloop
import tornado.httpserver

import textwrap


from tornado.options import define

define("port", default=8000, type=int, help='端口')


class Index_handler(tornado.web.RequestHandler):

    def get(self, args):

        # 返回URL路径中指定字符串的反转形式
        self.write(args[::-1])


class Test_handler(tornado.web.RequestHandler):

    # 到/wrap的POST请求将从参数text中取得指定的文本，并返回按照参数width指定宽度装饰的文本
    # 下面的请求指定一个没有宽度的字符串，所以它的宽度指定为程序中的程序中的get_argument的
    # 默认值40个字符串
    def get(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))


if __name__ == '__main__':

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[

        # 括号的含义是让tornado保存匹配里面表达式的字符串， 并将其作为一个请求方法的一个参数
        # 传递给RequestHandler类
        # 如果正则表达式中有一系列额外的括号，匹配的字符串将被按照在正则表达式中出现的顺序作为
        # 额外的参数传递进来
        (r"/reverse/(\w+)", Index_handler),
        (r"/wrap", Test_handler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()