# -*- coding:utf-8 -*-

import sys
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

if __name__ == '__main__':

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[

        # tornado在元祖中使用正则表达式来匹配HTTP请求的路径，这个路径是URL中主机后面的部分，
        # 不包括查询字符串和碎片， tornado吧这些正则表达式看作已经包含了行开始和结束锚点即
        # 字符串“/”被看作为“^/$”
        # 如果一个正则表达式包含一个捕获分组（即，正则表达式中的部分被括号括起来，匹配的内容将作为
        # 相应HTTP请求的参数传到RequestHandler对象中）
        (r"/", Index_handler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
