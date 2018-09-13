1安装GIT
    sudo apt-get install git
2注册帐号
3建立仓库
4生成公钥
    进入 .ssh文件夹
        ssh-keygen -t rsa -C “your_email@committermail.com”
5添加公钥
    网站中setting中 添加 .ssh目录中xxx.pub的内容复制粘贴 点击添加
6验证
    ssh -T git@github.com
7设置
    git config –global user.name “your_name” 
    git config –global user.email “your_email@youremail.com” 
8链接仓库
    git clone 仓库地址的复制链接
9命令
    git add xxx
    git commit -m 'xxx'
    git push origin master
