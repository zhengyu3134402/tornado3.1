# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import options, define
import os.path
import random

define('port', default=8000, type=int, help='端口')

# 渲染index13模板
class Index_handler(tornado.web.RequestHandler):

    def get(self):

        self.render('index13.html')

# 用于处理到/test13的POST请求
class Test13_handler(tornado.web.RequestHandler):

    # 将传入的文本分割成单词，然后创建一个字典，其中每个字母表的字符对应文本中的所有以其开头的单词
    # 在把这个字典和用户在替代文本中指定的内容一起传给模板文件test13.html
    def map_by_first_letter(self, text):

        mapped = dict()

        # 去除换行和回车
        for line in text.split('\r\n'):

            # 去除空格
            for word in [x for x in line.split(' ') if len(x) > 0]:
                #如果单词的首字母作为键不在字典中
                if word[0] not in mapped:

                    #那么以单词word的首字母为键的值为空
                    mapped[word[0]] = []
                #如果单词的首字母作为键在字典中，添加到值中
                mapped[word[0]].append(word)
        return mapped

    def post(self):

        source_text = self.get_argument('source')
        text_to_change = self.get_argument('change')
        source_map = self.map_by_first_letter(source_text)
        change_lines = text_to_change.split('\r\n')
        self.render('test13.html', source_map=source_map, change_lines=change_lines,
                    choice=random.choice)



if __name__ == '__main__':

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/', Index_handler),
        (r'/test13', Test13_handler),
    ], template_path=os.path.join(os.path.dirname(__file__), 'templates'),

        # static_path 参数指定了你应用到程序放置静态资源的(图像，css文件，javaScript)目录
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        # 测试模式，一旦python文件修改将自动重启文件
        debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
