# -*- coding:utf-8 -*-

# 目的：请求网站服务时能够创建和修改单词

import os
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
from pymongo import MongoClient

define('port', default=8000, type=int,help='port')

class Index(tornado.web.RequestHandler):

    def get(self):

        self.render('index21.html')

class Word_updata(tornado.web.RequestHandler):

    def post(self):

        self.render('word_updata21.html')



class Application(tornado.web.Application):

    def __init__(self):

        handlers = [(r'/w_c', Word_check),
                    (r'/', Index),
                    #(r'/(\w+)', Word_check),
                    (r'/word_updata_check', Word_updata_check),
                    (r'/word_updata', Word_updata),
                    (r'/word_f', Word_f),
                    ]

        client = MongoClient('localhost', 27017)

        db_name = client['word']

        self.data = db_name['word']
        #print(data.find_one({'word':'a'}))

        tornado.web.Application.__init__(self, handlers, debug=True,
                                         template_path=os.path.join(os.path.dirname(__file__), 'templates'))


class Word_updata_check(tornado.web.RequestHandler):

    def post(self):

        check_args = self.get_argument('key1', '')
        #print(check_args)

        coll = self.application.data


        word1 = coll.find_one({'word': check_args})




        #print(word1.keys())

        if not word1:

            self.write('字典中没有此键,请重新输入')
            #self.redirect('/w_c')

        else:
            del word1['_id']
            information = word1

            self.render('word_updata21.html', information=information,
                        check_args=check_args)


class Word_f(tornado.web.RequestHandler):

    def post(self):

        args = self.get_argument('change')


        coll = self.application.data

        data = coll.find_one({'word': 'b'})

        data['word'] = args
        #print(args)

        self.application.data.save(data)

        self.write('修改ok')









class Word_check(tornado.web.RequestHandler):

    def get(self, word_t):

        coll = self.application.data

        data = coll.find_one({'word': word_t})

        if data:

            del data['_id']

            self.write(data)

        else:
            self.set_status(404)
            self.write('未找到')

    def post(self):

        word1 = self.get_argument('word1', '0')
        #print(word1)

        change_word1 = self.get_argument('change_word1', '0')
        #print(change_word1)

        if  word1=='' and change_word1=='':

            self.write('请输入内容')

            self.redirect('/')

        else:

            if word1 and change_word1:

                self.write('不能同时查询和改变，输入一项即可')

            else:

                db = self.application.data
                if word1:


                    data = db.find_one({'word': word1})
                    if not data:
                        self.set_status(404)
                        self.write('没找到')
                    else:
                        del data['_id']

                        self.render('word_check21.html', data=data)

                elif change_word1:

                    data1 = db.find_one({'word': change_word1})

                    #del data1['_id']
                    #print(data1)

                    if not data1:

                        self.write('没找到单词，无法修改')

                    else:

                        del data1['_id']

                        self.render('word_change21.html', data1=data1)










if __name__ == '__main__':

    tornado.options.parse_command_line()

    http_server = tornado.httpserver.HTTPServer(Application())

    http_server.listen(options.port)

    tornado.ioloop.IOLoop.instance().start()
