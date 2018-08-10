# -*- coding:utf-8 -*-

from tornado.template import Template

def dis(a):
    return ''.join([x for x in a if x not in 'aeiou'])

print(dis('abced'))

print(Template("my name is {{ d('mortimer') }}").generate(d=dis))