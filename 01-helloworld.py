# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import tornado.httpserver
import tornado.ioloop

# 从命令行中读取设置，指定我们的应用监听HTTP请求的端口
import tornado.options
import tornado.web
from tornado.options import define, options

# 如果一个与define语句中同名的设置在命令行中被给出，那么它将成为全局options的一个属性
# 使用命令 python xxx --help 会打印出所有定义的选项以及在define函数的help参数中指定的文本
# 若没有写出命令选项指定值，则使用default的值进行代替
# 使用type参数进行基本的参数类型验证，当不适合类型被给出时候会抛出个异常
define("port", default=8000, help="a base", type=int)

# tornado的请求处理类函数
# 当处理请求时，tornado将这个类实例化，并调用HTTP请求方法所对应的方法
class Index_handler(tornado.web.RequestHandler):

    # 对HTTP的GET请求作出响应
    def get(self):
        # 从一个查询字符串中取得参数，如果没有这使用第二个参数作为默认值
        a = self.get_argument('a', 'hello')
        # write方法 以一个字符串作为函数的参数，将其写入到HTTP响应中
        self.write(a + ' friedly user!')

if __name__ == "__main__":

    # 解析命令行
    tornado.options.parse_command_line()

    # 创建了Application类的实例,传递给Application类__init__方法的最重要的参数是handlers
    # 它告诉tornado用哪个类来响应请求
    app = tornado.web.Application(handlers=[

        (r"/", Index_handler),
    ])

    # 一旦Application对象被创建， 我们可以将其传递给Tornado的HTTPServer对象
    http_server = tornado.httpserver.HTTPServer(app)

    # 使用在命令行指定的 端口进行监听（通过options对象取出）
    http_server.listen(options.port)

    # 在程序准备好接受HTTP请求后， 创建了一个tornado的IOLoop的实例
    tornado.ioloop.IOLoop.instance().start()




