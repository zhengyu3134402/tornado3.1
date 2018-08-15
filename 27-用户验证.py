# -*- coding:utf-8 -*-

import os.path
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver

from tornado.options import define, options
define('port', default=8000, help='port', type=int)

class Base_handler(tornado.web.RequestHandler):

    def get_current_user(self):

        return self.get_secure_cookie("username")

class Login_handler(Base_handler):

    def get(self):
        self.render('login27.html')

    def post(self):

        self.set_secure_cookie("username", self.get_argument("username"))
        self.redirect("/")

class Welcome_handler(Base_handler):

    # 为了使用tornado的认证功能，我们西药对登录用户标记具体的处理函数。可以使用
    #  @tornado.web.authenticated装饰器
    #  使用这个转世其包裹一个处理方法时候，tornado 将确保这个方法的主体只有在合法用户
    #  被发现时才会被调用，这个类只对已登录用户渲染index27.html模板
    # 在get 方法被调用之前，authenticated装饰器确保current_user属性有值。
    # 如果current_user值为假, 任何GET或HEAD请求都将把访客重定向到应用设置中login_url
    #  指定的URL 非发用户的POST请求将返回一个带有403状态的HTTP响应

    # authenticated装饰器依赖于 current_user属性和login_url设置
    #   current_user属性
    #    用来存储为当前请求进行用户验证的标识，默认值为None， 为了authenticated转世其
    #    能够成功标识一个已经认证用户， 你必须覆写请求处理程序中默认的get_current_user()
    #    方法来返回当前用户
    @tornado.web.authenticated
    def get(self):
        self.render('index27.html', user=self.current_user)

class Logout_Handler(Base_handler):

    def get(self):

        if (self.get_argument("logout", None)):

            self.clear_cookie("username")
            self.redirect("/")

if __name__ == '__main__':

    tornado.options.parse_command_line()

    settings = {

        "template_path": os.path.join(os.path.dirname(__file__), 'templates'),
        "cookie_secret": "keys",
        "xsrf_cookies": True,

        # login_url是应用登录表单的地址， 如果get_current_user方法返回了一个假值，
        #  带有authenticated装饰器的处理程序将重定向浏览器的URL以便登录
        # 当tornado构建重定向URL时，它还会查询字符串添加一个next参数，其中包含了发起
        #  重定向登录页面的URL资源地址。可以使用
        #  self.redirect(self.get_argument('next', '/'))这样的行来重定向登录后用户
        #  回到的页面
        "login_url": "/login",

    }

    app = tornado.web.Application([

        (r'/', Welcome_handler),
        (r'/login', Login_handler),
        (r'/logout', Login_handler),
    ], debug=True, **settings)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
