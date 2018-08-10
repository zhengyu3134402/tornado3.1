from tornado.template import Template

print(Template("{{ 1+1 }}").generate())

print(Template("{{ 'scrambled eggs'[-4:] }}").generate())

print(Template("{{ ','.join([str(x*x) for x in range(10)]) }}").generate())
