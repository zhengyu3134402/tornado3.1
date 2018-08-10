from tornado.template import Template

content = Template("<html><body><h1>{{ header }}</h1></body></html>")

print(content.generate(header="welcome"))
