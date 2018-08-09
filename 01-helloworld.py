# -*- conding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8000, help="a base", type=int)

class Index_handler(tornado.web.RequestHandler):

    def get(self):

        a = self.get_argument('a', 'hello')
        self.write(a + ' friedly user!')

if __name__ == "__main__":

    tornado.options.parse_command_line()
    app = tornado.web.Application([

        (r"/", Index_handler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()