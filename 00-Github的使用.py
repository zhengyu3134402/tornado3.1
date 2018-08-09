# -*- coding:utf-8 -*-

# Github

# 目的 :借助Github托管项目代码

# 仓库（Repository）：存放项目代码，每个项目对应一个仓库，多个开源项目有多个仓库

# 收藏（收藏项目，方便瞎猜查看）

# 复制克隆项目（fork）：该fork的项目是独立存在的

# 事物卡片（lssue）：发现代码BUG，但是目前没有成形代码，需要讨论时用

# Github主页 仓库主页  个人主页

# 注册github帐号

# 官方网址 github.com

# sign up 注册 注册之后的页面
# 选择仓库
    # 免费仓库
    # 私有仓库收费
# 点击默认

# 然后出现用户调查页面 点击跳过

# 脚下留心

    # 1因为github在国外服务器所有访问较慢或则无法访问，需要翻墙
    # 2私有仓库权限 收费
    # 3新注册用户必须验证邮箱后才可以创建git库仓库
        # 进入页面重新发送邮件
        # qq邮箱需要设置白名单才会收到邮件
            # qq邮箱点击设置点击反垃圾 点击设置域名白名单 github.com添加到其中


# 创建仓库

    # 1个git库对应一个开源项目

    # Repository name 仓库名称
    # Description 项目描述
    # Public 公共仓库
    # Private 私有仓库
    # Initialize this repository with a README 创建README文件项目详细描述


# 仓库主页
    # Edit 修改描述

    # Create new file 创建文件
    # Upload files 上传文件
    # Find file 搜索仓库文件

    # Watch  关注
    # Star 收藏
    # Fork 复制克隆项目

    # Clone or download 直接下载或则通过git克隆

    # Issues 新建issue

# 仓库管理

    # create new file 点击创建文件

# Github lssues

# git安装和使用

    # 目的：通过git管理github项目


# 使用

    # 1添加远程ssh_key

     # 创建项目ssh key（本地仓库和GitHub仓库之间的传输是通过SSH加密的）

        # ssh-keygen -t rsa -C "youremail@example.com"
        # 在.ssh/目录下会生成两个文件 id_rsa是私钥， id_rsa.pub是公钥

        # github主页打开settings的SSH Key页面，点击New SSH Key 填上任意Title
        # 在key的文本框里粘贴id_rsa.pub文件内容，点击"Add Key"

    # 2新建仓库

    # 3从远程克隆仓库

        # 初始化变量 user.name  和 user.email
            # git config --global user.name ''
            # git config --global user.email xx@xxx.com

        # 点击Clone or download
         # 复制如git@github.com:zhengyu3134402/tornado3.1.git
         # 选择目录 运行命令 git clone git@github.com:zhengyu3134402/tornado3.1.git

    # 4 与github库交互

        # 将github库获取到本地
            # git pull

        # 将本地库提交到github库
            # git push origin master

        # git init 获取本地仓库目录


# 本地仓库

    # 工作区

    # 暂存区

    # 仓库区

    # 若本机添加一个文件

        # 1 将文件添加到暂存区
            # git add 文件(若为目录 则 目录名/)

        # 2 将文件添加到仓库里
            # git commit -m '文件描述'

        # 3 将文件添加到github仓库
            # git push origin master

        # git log 查看历史记录 （简介的查看历史记录 git log --pretty=oneline）

    # 从github仓库获取内容

        # git pull

    # 历史版本操作

        # 1 从仓库把内容拿到暂存区
            # git reset 版本号（git log --pretty=oneline查看版本号）
            # 或者
            # git reset HEAD^ 文件名(HEAD^:上一个版本，HEAD^^(或者直接写HEAD～1,HEAD～2))

        # 2 将暂存区的内容放到本地
            # git checkout 文件名

#   总结

    # 从github初始化本地项目:git clone
        # 本地操作 git add, git commit, git push oringin master

    # 从github同步：git pull
    # 历史版本 git reset 版本号， git checkout 文件名

    # 查看历史操作: git log(git log --pretty=oneline)
    # 查看暂存区信息：git status