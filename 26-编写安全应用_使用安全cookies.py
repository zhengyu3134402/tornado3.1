# -*- coding:utf-8 -*-

# tornado的set_secure_cookie()和get_secure_cookie()函数发送和取得浏览器cookies,
#  防范浏览器中的恶意修改，必须在应用的构造函数中指定cookie_secret参数

# tornado将cookie值编码为Base-64字符串，并添加了一个时间戳和一个cookie内容的HMAC签名，
#  若cookie的时间戳太旧（或来自未来），或签名和期望值不匹配，get_secure_cookie()函数
#  会认为cookie已经被篡改， 并返回None，好像cookie没有被设置过一样


# HTTP-Only 和 SSL Cookies
# 可以通过值允许SSL连接的方式减少cookie值在网络中被截取的可能性，可以改以让浏览器对JavaScript
#  隐藏cookie值， 为cookie设置secure属性来指示浏览器值荣果ssl连接传递cookie， httponly属性
#  这个属性实行浏览器对于JavaScript不可访问cookie，可以防范来自子读取cookie值的跨站脚本攻击
#  为了开启这些功能，可以想set_cookie 和set_secure_cookie方法传递关键字参数，如一个安全的
#  HTTP-only cookie(不是tornado的签名cookie)可以调用
#  self.set_cookie('foo','bar', httponly=True, secure=True)发送

# xsrf令牌和AJAX请求



import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import define, options

define('port', default=8000, help='port', type=int)

class Index_handler(tornado.web.RequestHandler):

    def get(self):

        cookie = self.get_secure_cookie('count')

        if not cookie:

            self.set_secure_cookie('count', 'a')

        print(cookie)


if __name__ == '__main__':

    tornado.options.parse_command_line()

    # 传递给Application构造函数的cookie_secret值应该是唯一的随机字符串
    settings = {

        "cookie_secret": 'xxxxx',
        # 并在模板中
        # {% raw xsrf_form_html() %}
        "xsrf_cookies": True,

        'debug': True,
    }

    app = tornado.web.Application(handlers=[

        (r'/', Index_handler),
    ], **settings)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
