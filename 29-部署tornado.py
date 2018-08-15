# -*- coding:utf-8 -*-

# 我们碰到的问题是当同步函数调用块时， 设想在一个tornado执行的数据库查询或磁盘访问块中，进程不允许
#  回应新的请求， 这个问题最简单的解决方法是运行多个解释器的实例。通常清空下，会使用一个方向代理，
#  如Nginx， 来非匹配多个Tornado实例的加载

# 使用Nginx作为方向代理
    # 一个代理服务器是一台中转客户端资源请求到适当的服务器的机器。一些网络安装使用代理服务器过滤
    # 或缓存本地网络机器到internet的HTTP请求。因为我们将运行一些在不同TCP端口上的Tornado实例
    # 因此我们使用反响代理服务器， 客户端通过internet 连接一个反向代理服务器，然后反向代理服务
    # 器发送tingi到代理后端的Tornado服务器池中的任何一个主机。代理服务器被设置为对客户端透明的，
    # 当他会像上有的tornado节点传递一些有用的信息，如原始客户端IP地址和TCP格式

'''
 Nginx基本配置

# 假设系统使用了epoll
# Nginx默认以循环的方式分配请求，也可以选择基于客户端的ip地址分配请求


 user nginx;
 worker_processes 5;
 error_log /var/log/nginx/error.log;
 pid /var/run/nginx.pid;
 events {
   worker_connections 1024;
   use epoll;
 }
 proxy_next_upstream error;
 upstream tornadoes {
   server 127.0.0.1:8000
   server 127.0.0.1:8001;
   server 127.0.0.1:8002;
   server 127.0.0.1:8003;
   }
# Nginx服务器在80端口监听连接，然后分配这种请求给upstream服务器
#  组中列出的Tornado实例

 server {
   listen 80;
   server_name www.example.org *.example.org;

   # location /static/指令， 它告诉Nginx直接提供静态目录的文件，而不再代理请求到Tornado
   # Nginx比tornado更高效的提供静态文件，所以减少tornado进程中不必要的加载是非常有意义的
   location /static/ {
       root /var/www/static;
       if ($query_string) {
           expires max;
       }
   }

# Nginx把位于location指令中的字符串看作是一个以行使锚点开始，任何字母重复结束的正则表达式。
# 所以/被看作是表达式^/.* 当Nginx匹配这些字符串时候，像/statcic这样的更加特殊的字符串在像/
# 这样更加通用的字符串之前被检查
 location / {
       proxy_pass_header Server;
       proxy_set_header Host $http_host;
       proxy_redirect off;
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Scheme $scheme;

       # proxy_pass指令指定接受转发请求的服务器URI，可以在proxy_pass URI中的
       # 主机部分引用upstream服务器组的名字
       proxy_pass http://tornadoes;

       }
   }
'''

# Nginx的SSL解密

# 大部分主要的社交网络应用都默认或作为用户可配置选项使用安全协议。同时我们使用Nginx
#  解密传入的SSL加密请求，然后吧解码后的HTT·请求分配给上有服务器

# 例子
    # 用于将解密传入的HTTPS请求的server块，并使用代码例子中我们使用过的代理指令转发解密后的通信
    # 使用SSL的server块
"""
        server {
            
            # 将标准HTTPS的443端口监听安全Web请求外
            listen 443;
            ssl on;
            ssl_certificate /path/to/cert.pem;
            ssl_certificate_key /path/to/cert.key;
            default_type application/octet-stream;
            location /static/ {
            root /var/www/static;
            if ($query_string) {
            expires max;
                }
            }
            location = /favicon.ico {
            rewrite (.*) /static/favicon.ico;
            }
            location / {
            proxy_pass_header Server;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Scheme $scheme;
            proxy_pass http://tornadoes;
            }
        }
"""

# 用于重定向HTTP请求到安全渠道的server块

# server {
#    listen 80;
#    server_name example.com;
#    rewrite /(.*) https://$http_host/$1 redirect;
#}



# 使用Supervisor监控Tornado进程

  # 监控和控制多进程

  # supervisor的设计是每次开机时候启动其配置文件中列出的进程。我们将看到管理我们在Nginx
  # 配置文件中作为上游主机提到4个Tornado实例的Superivisor配置， 典型的supervisord.conf
  # 文件中包含了全局的配置指令， 并加载conf.d目录下的其他配置文件
'''
# 安装和配置好Supervisor，可以使用supervisortctl管理supervisord进程
# 命令： update , stopped ,updated process group ,status
# 定义了4个程序 分别命名为tornado-8000到tornado-8003
# pprgrams 部分定义了Supervisor将要运行的每个命令的参数
# 为了一起管理所有的tornado 进程，创建一个组是很有必要的
# 要管理我们的tornado应用时候，通过带有通配符的组名引用所有的组成程序
# 重启应用： zai supervisorctl工具中使用命令restart tornadoes:*

# 声明了一个叫tornadoes的组，并在其中列出了每个程序
[group:tornadoes]
programs=tornado-8000,tornado-8001,tornado-8002,tornado-8003

[program:tornado-8000]
# command的值是必须的，通常带有我们希望监听的port参数的Tornado应用
# 还为每个程序的工作目录, 有效用户和日志文件定义了额外的设置，而吧autorestart和
#  redirect_stderr设置为true 是非常有用的
# 不想管错误码 autorestart = true
command=python /var/www/main.py --port=8000
directory=/var/www
user=www-data
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log
loglevel=info

[program:tornado-8001]
command=python /var/www/main.py --port=8001
directory=/var/www
user=www-data
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/tornado.log
loglevel=info

[program:tornado-8002]
command=python /var/www/main.py --port=8002
directory=/var/www
user=www-data
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/tornado.log
loglevel=info

[program:tornado-8003]
command=python /var/www/main.py --port=8003
directory=/var/www
user=www-data
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/tornado.log
loglevel=info
'''
