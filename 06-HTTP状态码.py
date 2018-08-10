# -*- coding:utf-8 -*-

import sys
import tornado.web
import tornado.options
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options
reload(sys)
sys.setdefaultencoding('utf-8')

define('port', default=8000, type=int, help='端口')

class Index_handler(tornado.web.RequestHandler):

    def get(self):

        # 显示地设置HTTP状态码
        # 某些情况下 tornado会自动地设置HTTP状态码:
            # 404
                # NOT Found tornado 会在请求路径无法匹配任何RequestHandler类相对应的
                # 模式时候返回404响应码
            # 400
                # Bad Request 如果调用了一个没有默认的get_argument函数，并且没有发现诶定名称的参数
                # 返回一个400的响应码
            # 405
                # Method Not Allowed 如果传入的请求使用了RequestHandler中没有定义的
                # HTTP方法（比如，一个POST请求，但处理函数中没有定义post方法），会返回一个405状态码
            # 500
                # Internal Server Error当程序遇到任何不能让其推出的错误时，Tornado将返回
                # 500响应码，代码中没有捕获任何异常也会导致500响应码
            # 200
                # 如果响应成功， 并且没有其他返回码被设置，Tornado将默认返回一个 200（ok）响应码
        #self.set_status(200, 'good')

        self.write('ok1111')


    # 如果想用自己的方法代替默认的错误响应，可以重写write_error方法在你的RequestHandler类中
    def write_error(self, status_code, **kwargs):

        self.write('你的响应码为%d'%status_code)


if __name__ == '__main__':

    tornado.options.parse_command_line()

    app = tornado.web.Application(handlers=[

        (r'/', Index_handler),
    ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()


