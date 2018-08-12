# -*- coding:utf-8 -*-

# MongoDB数据库

    # NoSQL简介

        # 非关系型数据库
        # 内存级的数据读写

    # Mongodb数据库
        # 分布式文件存储的NoSQL数据库

    # Mongodb数据库特点

        # 模式自由： 存储不同结构的文档在一个数据库里
        # 面向集合的存储：适合存储JSON风格文件的形式
        # 完整的索引支持：对任何属性可索引
        # 复制和高可用性：支持服务器之间的数据复制
        # 自动分片：支持云级别的伸缩型，支持水平的数据库集群，可动态添加额外的机器
        # 丰富的查询：查询指令使用JSON形式的标记
        # 快速接地的更新：查询优化器会分析查询表达式，形成一个高级的查询计划
        # 高效传统存储方式：支持二进制数据库及大型对象（图片）

    # Mongodb的名词


        # database 数据库
        # collection 数据库表集合
        # document 集合当中的一个数据
        # field 数据字段域
        # index 索引
        # MongoDB不支持表的连接
        # primary key 主键MongoDB自动将_id字段设置为主键

    # Mongodb三元素

        # 集合collection就是关系库中的表
        # document文档对应着关系库中的行

    # MongoDB文档

        # 就是一个对象，有键值对组成 是json的扩展Bson形式（专门用于MongoDb的数据）
        # {'a':'b','c':'d'}

        # 集合：类是于关系型数据库中的表，储存多个文档，结构不固定

    # MongoDB安装

        # 两点注意 版本的基数为开发版本，偶数为稳定版本

        # 1 sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

        # 2 echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

        # 3 sudo apt-get update

        # 4 sudo apt-get install -y mongodb-org

        # sudo service mongod stop　　#停止服务
        # sudo service mongod start　　#启动服务
        # sudo service mongod restart #重新启动服务
        # sudo service mongod status #查看状态

        # 允许开机启动

            # systemctl enable mongod

        # 进入mongodb

            # mongo

        # mongodb的配置文件

            # less /etc/mongod.conf

        # 允许外部连接的方法

            # 修改mongod.conf 中的 bindIP改为 0.0.0.0
            # 重启mongodb

    # 服务端命令 mongod

    # 客户端命令 mongo

        # 默认用test数据库

        # 数据库 操作命令

            # db ：提示当先使用的数据库
            # db.stats():查看当前数据库信息
            # show dbs:查看当前所有的数据库
            # use 数据库名称:切换到某个数据库（moangodb不需要创建数据库）
            # db.dropDatebase(): 删除当前指向的数据库

        # 创建集合的操作命令

            # db.createCollection(name, options)
                # name:创建集合的名称
                # options是一个文档，用于指定集合的配置（可选）

                    # 例子
                        # 不限制集合大小的创建
                            # db.createCollection('a')

                        # 限制结合大小的创建
                            # db.createCollection{"sub", {capped:true, size:10}}
                                # capped默认false表示不设置上限，值为true表示设置上限
                                # size表示上限的大小，当文档达到上限时候，会将之前的数据覆盖，单位字节

                    # 关于size的示例

                        # db.createCollection("sub", {capped:true, size:10})

                        #插入第一条数据

                            # db.sub.insert({title:'linux',count:10})

                        # ........

                        # 当添加的内容超过size的大小， 添加新的内容会覆盖掉最老的内容



        # 查看当前数据库集合

            # show collections

        # 删除集合

            # db.集合名称.drop()

        # 集合里插入文档

            # db.集合名称insert(document)

        # 查看集合中的文档

            # db.集合名称.find()

        # 修改集合当中的文档
                                                # multi:flale 默认在查到多数据
                                                # 中只修改一行，设置为True修改多行
            # db.集合名称.update(修改的数据，改为什么, {multi:True})_

        # 指定属性更新，通过操作符 $set

            # db.stu.insert({a: '1'},{b: '2'})
            # db.update({a:'1'},{$set:{a:'3'}})

        # 文档的保存

            # 如果文档的id存在的话执行修改的操作，如果文档的id不存在则执行添加的操作

        # 删除文档

            # justOne 如果为True或1 贼删除一条，默认False，表示删除多条
            # db.集合名称.remove(删除的数据, jsutOne:False)

            # 全部删除 db.stu.remove({})


    # MongoDB支持的数据类型

        # Object id：文档ID

            # 唯一标识主键
            # 是一个12字节的十六进制
                # 前4个字节为当前时间错
                # 接写来3个字节为机器ID
                # 接下来2个字节为MongoDB服务进程id
                # 最后3个字节是简单的增量值

        # Stirng: 字符串，最常用，必须是有效的UTF-8
        # Boolean: 布尔值
        # Integer: 整数可以是32位或64位
        # Double: 浮点值
        # Arrays: 数组或列表，多个值存储到一个键
        # Object: 用于嵌入式的文档，即一个值为一个文档（取代关系）
        # Null: Null值
        # timestamp: 时间戳
        # Date: 存储当前日期或时间的UNIX时间格式

    # 查询

        # find

            # db.集合名称.find({查询条件}) 返回符合查询条件的所有数据

            # db.集合名称.findOne({查询条件}) 返回符合查询条件的一条数据

            # db.集合名称.find({查询条件}).pretty() 格式化返回来的数据（容易看）

        # 比较运算符

            # 等于 没有运算符

            # 小于 $it

            # 小于或等于 $ite

            # 大于 $gt

            # 大于或等于 $gte

            # 不等于 $ne

               # db.stu.find({age:{$gte:10}})

        # 逻辑运算符

            # 逻辑与  默认

            # 逻辑或  $or

                # db.stu.find({$or:[{age:{$gt:18}},{gender:1}]})

            # and 和 or 一起用

                # db.sut.find({$or:[{age:{$gte:18}},{gender:1}],name:'gj'})

        # 范围运算符

            # 使用 $in  $nin

                # db.stu.find({age:{$in:[18,28]}})

        # 支持正则表达式

            # 使用//或$regex编写正则表达式

                # db.stu.find({name:/^红/})
                # sb.stu.find({name:{$regex:'^黄'}})

        # 自定义查询

            # 使用 $where 后面写一个函数，返回满足条件的数据

                # db.stu.find({$where:function(){return this.age>20}})

        # 限制Limit

            # 用于读取指定数量的文档

              # db.集合名称.find().limit(数字)

        # 跳过多少条skip

            # 用于跳过指定数量的文档

                # db.集合名称.find().skip(数字)

        # 投影

            # 一个文档有5个字段，需要显示3个，投影3个字段即可

                # 对于显示的字段，设置为1即可,对于主键 _id:0
                # db.集合名称.find({},{字段名称:1,..})

                    # db.stu.find({},{name:1,gender:1})

        # 排序

            # sort()用于对结果进行排序

                # 参数为1为升序排列
                # 参数为-1降序排列
                # db.集合名称.find().sort({字段：1,..})

        # 统计个数

            # 方法count()用于统计结果集中文档条数

                # db.集合名称.find({条件}).count()

        # 消除重复

            # distinct()对数据进行去重

                # db.集合名称.distinct('去重字段',{条件})

        # 聚合 aggregate


            # 常用管道

                # $group:将集合中的文档分组，可用于计算结果

                    # $group
                    # 将集合中的文档分组，可用于统计结果
                    # _id表示分组的依据，使用某个字段的格式为'$字段'
                    #例1：统计男生、女生的总人数
                    # db.stu.aggregate([
                    #    {$group:{id:'$gender',counter:{$sum:1}}}])

                    # Group by null
                    # 将集合中所有文档分为一组
                    # 例2：求学生总人数、平均年龄
                    # db.stu.aggregate([{$group:{_id:null,counter:{$sum:1},avgAge:{$avg:'$age'}}}])
                    # 透视数据
                    # 例3：统计学生性别及学生姓名
                    # db.stu.aggregate([{$group:{_id:'$gender',name:{$push:'$name'}}}])
                    # 使用$$ROOT可以将文档内容加入到结果集的数组中，代码如下
                    # db.stu.aggregate([{$group:{_id:'$gender',name:{$push:'$$ROOT'}}}])

                # $match:过滤数据，只输出符合条件的文档


                    #例1：查询年龄大于20的学生
                    #db.stu.aggregate([{$match:{age:{$gt:20}}}])
                    #例2：查询年龄大于20的男生、女生人数
                    #db.stu.aggregate([{$match:{age:{$gt:20}}},{$group:{_id:'$gender',counter:{$sum:1}}}
                    #])
                # $project:修改输入文档的结构，如重命名，增加，删除字段，创建计算结果

                    # 例1：查询学生的姓名、年龄
                    # db.stu.aggregate([{$project:{_id:0,name:1,age:1}}])
                    # 例2：查询男生、女生人数，输出人数
                    # db.stu.aggregate([{$group:{_id:'$gender',counter:{$sum:1}}},{$project:{_id:0,counter:1}}
                    # ])
                # $sort:将输入文档排序后输出

                    #例1：查询学生信息，按年龄升序
                    #b.stu.aggregate([{$sort:{age:1}}])
                    #例2：查询男生、女生人数，按人数降序
                    #db.stu.aggregate([{$group:{_id:'$gender',counter:{$sum:1}}},{$sort:{counter:-1}}
                    # ])
                # $limit:限制聚合管道返回的文档数

                    #db.stu.aggregate([{$limit:2}])

                # $skip:跳过指定数量的文档，并返回余下的文档

                    # 例2：查询从第3条开始的学生信息
                    # db.stu.aggregate([{$skip:2}])
                    # 例3：统计男生、女生人数，按人数升序，取第二条数据
                    # db.stu.aggregate([
                    #   {$group:{_id:'$gender',counter:{$sum:1}}},
                    #    {$sort:{counter:1}},
                    #    {$skip:1},
                    #    {$limit:1}
                    # ])
                    # 注意顺序：先写skip，再写limit
                # $unwind:将数组类型的字段进行拆分

                    #对某字段值进行拆分
                   # db.集合名称.aggregate([{$unwind:'$字段名称'}])
                   # 构造数据
                   # db.t2.insert({_id:1,item:'t-shirt',size:['S','M','L']})
                   # 查询
                   # db.t2.aggregate([{$unwind:'$size'}])
                   # 语法2
                   # 对某字段值进行拆分
                   # 处理空数组、非数组、无字段、null情况
                   # db.inventory.aggregate([{
                   #     $unwind:{
                   #         path:'$字段名称',
                   #         preserveNullAndEmptyArrays:<boolean>#防止数据丢失
                   #     }
                   # }])
                   # 构造数据
                   # db.t3.insert([
                   # { "_id" : 1, "item" : "a", "size": [ "S", "M", "L"] },
                   # { "_id" : 2, "item" : "b", "size" : [ ] },
                   # { "_id" : 3, "item" : "c", "size": "M" },
                   # { "_id" : 4, "item" : "d" },
                   # { "_id" : 5, "item" : "e", "size" : null }
                   # ])
                   # 使用语法1查询
                   # db.t3.aggregate([{$unwind:'$size'}])
                   # 查看查询结果，发现对于空数组、无字段、null的文档，都被丢弃了
                   # 问：如何能不丢弃呢？
                   # 答：使用语法2查询
                   # db.t3.aggregate([{$unwind:{path:'$sizes',preserveNullAndEmptyArrays:true}}])#

            # 表达式

                # $列名

                # 常用表达式

                  #  $sum: 计算总和
                  #  $avg: 计算平均值
                  #  $min: 获取最小值
                  #  $max: 获取最大值
                  #  $push: 在文档中插入值到一个数组中
                  #  $first: 根据资源文档的排序获取第一个文档数据
                  #  $last: 根据资源文档的排序获取最后一个文档数据

            # db.聚合名称.aggregate([{管道：{表达式}}])

'''
    超级管理员
    为了更安全的访问mongodb，需要访问者提供用户名和密码，于是需要在mongodb中创建用户
    采用了角色-用户-数据库的安全管理方式
    常用系统角色如下：
    root：只在admin数据库中可用，超级账号，超级权限
    Read：允许用户读取指定数据库
    readWrite：允许用户读写指定数据库
    创建超级管理用户
    use admin
    db.createUser({
        user:'admin',
        pwd:'123',
        roles:[{role:'root',db:'admin'}]
    })
    启用安全认证
    修改配置文件
    sudo vi /etc/mongod.conf
    启用身份验证
    注意：keys and values之间一定要加空格, 否则解析会报错
    security:
      authorization: enabled
    重启服务
    sudo service mongod stop
    sudo service mongod start
    终端连接
     mongo -u 'admin' -p '123' --authenticationDatabase 'admin'
    普通用户管理
    使用超级管理员登录，然后进入用户管理操作
    查看当前数据库的用户
    use test1
    show users
    创建普通用户
    db.createUser({
        user:'t1',
        pwd:'123',
        roles:[{role:'readWrite',db:'test1'}]
    })
    终端连接
    mongo -u t1 -p 123 --authenticationDatabase test1
    切换数据库，执行命令查看效果

    修改用户：可以修改pwd、roles属性

    db.updateUser('t1',{pwd:'456'})

    复制（副本集）
    什么是复制
    复制提供了数据的冗余备份，并在多个服务器上存储数据副本，提高了数据的可用性，并可以保证数据的安全性
    复制还允许从硬件故障和服务中断中恢复数据
    为什么要复制
    数据备份
    数据灾难恢复
    读写分离
    高（24* 7）数据可用性
    无宕机维护
    副本集对应用程序是透明
    复制的工作原理
    复制至少需要两个节点A、B...
    A是主节点，负责处理客户端请求
    其余的都是从节点，负责复制主节点上的数据
    节点常见的搭配方式为：一主一从、一主多从
    主节点记录在其上的所有操作，从节点定期轮询主节点获取这些操作，然后对自己的数据副本执行这些操作，从而保证从节点的数据与主节点一致
    主节点与从节点进行数据交互保障数据的一致性
    复制的特点
    N 个节点的集群
    任何节点可作为主节点
    所有写入操作都在主节点上
    自动故障转移
    自动恢复
    设置复制节点
    接下来的操作需要打开多个终端窗口，而且可能会连接多台ubuntu主机，会显得有些乱，建议在xshell中实现
    step1:创建数据库目录t1、t2
    在Desktop目录下演示，其它目录也可以，注意权限即可
    mkdir t1
    mkdir t2
    step2:使用如下格式启动mongod，注意replSet的名称是一致的
    mongod --bind_ip 192.168.196.128 --port 27017 --dbpath ~/Desktop/t1 --replSet rs0
    mongod --bind_ip 192.168.196.128 --port 27018 --dbpath ~/Desktop/t2 --replSet rs0
    step3:连接主服务器，此处设置192.168.196.128:27017为主服务器
    mongo --host 192.168.196.128 --port 27017
    step4:初始化
    rs.initiate()
    初始化完成后，提示符如下图：
    初始化

    step5:查看当前状态
    rs.status()
    当前状态如下图：
    初始化

    step6:添加复本集
    rs.add('192.168.196.128:27018')
    step7:复本集添加成功后，当前状态如下图：
    初始化

    step8:连接第二个mongo服务
    mongo --host 192.168.196.128 --port 27018
    连接成功后，提示符如下图：
    初始化

    step9:向主服务器中插入数据
    use test1
    for(i=0;i<10;i++){db.t1.insert({_id:i})}
    db.t1.find()
    step10:在从服务器中插查询
    说明：如果在从服务器上进行读操作，需要设置rs.slaveOk()
    rs.slaveOk()
    db.t1.find()
    其它说明
    删除从节点
    rs.remove('192.168.196.128:27018')
    关闭主服务器后，再重新启动，会发现原来的从服务器变为了从服务器，新启动的服务器（原来的从服务器）变为了从服务器


    分片
    在Mongodb里面存在另一种集群，就是分片技术,可以满足MongoDB数据量大量增长的需求
    当MongoDB存储海量的数据时，一台机器可能不足以存储数据，也可能不足以提供可接受的读写吞吐量，这时，我们就可以通过在多台机器上分割数据，使得数据库系统能存储和处理更多的数据
    为什么使用分片
    本地磁盘不够大
    当请求量巨大时会出现内存不足。
    垂直扩展价格昂贵(内存、磁盘、cpu)
    实现分片
    分片结构图如下：
    分片

    实现分片需要3部分：
    路由服务器mongos：客户端由此接入，根据分片依据，将数据写入到不同的数据服务器
    配置服务器mongod：将数据进行分片的依据
    数据服务器mongod：可以有多台物理机，用于存储实际的数据块
    设计端口如下：
    路由服务器：60001
    配置服务器：60002
    数据服务器1：60003
    数据服务器2：60004
    step1:启动数据服务器，当前位于Desktop目录下
    sudo mkdir t1
    sudo mkdir t2
    sudo mongod --port 60003 --dbpath=~/Desktop/t1
    sudo mongod --port 60004 --dbpath=~/Desktop/t2
    step2:启动配置服务器
    sudo mkdir conf
    sudo mongod --port 60002 --dbpath=~/Desktop/conf
    step3:启动路由服务器
    sudo mongos --port 60001 --configdb 192.168.196.128:60002
    step4:在路由服务器中添加数据服务器
    mongo --port 60001
    use admin
    db.runCommand({addshard:'192.168.196.128:60003'})
    db.runCommand({addshard:'192.168.196.128:60004'})
    step5:对数据库test1启用分片
    db.runCommand({enablesharding:'test1'})
    step6:指定片键，即集合中文档的分片依据
    db.runCommand({shardcollection:'test1.t1',key:{name:1}})
    step7:测试数据，向集合中插入1W条数据
    for(i=0;i<10000;i++){
        db.t1.insert({name:'abc'+i})
    }
    step8:查看数据存储情况
    db.printShardingStatus()
    可以查看到数据均匀存储在了数据服务器上
    step9:查询数据
    db.t1.find({name:'abc1000'})
    db.t1.find({name:'abc9000'})
    分片的使用，对于客户端是透明的，对数据的读写没有变化



    备份
    语法
    mongodump -h dbhost -d dbname -o dbdirectory
    -h：服务器地址，也可以指定端口号
    -d：需要备份的数据库名称
    -o：备份的数据存放位置，此目录中存放着备份出来的数据
    例1
    sudo mkdir test1bak
    sudo mongodump -h 192.168.196.128:27017 -d test1 -o ~/Desktop/test1bak
    恢复
    语法
    mongorestore -h dbhost -d dbname --dir dbdirectory
    -h：服务器地址
    -d：需要恢复的数据库实例
    --dir：备份数据所在位置
    例2
    mongorestore -h 192.168.196.128:27017 -d test2 --dir ~/Desktop/test1bak/test1


    MapReduce
    ```


    Google在2003年到2004年公布了关于GFS、MapReduce和BigTable三篇技术论文，这也成为后来云计算发展的重要基石，

    谷歌技术有"三宝"，GFS(分布式文件系统)、MapReduce编程模型(Map映射和Reduce归约）和BigTable(分布式数据存储系统)！

    `Map-Reduce`是一种计算模型，简单的说就是将大批量的工作（数据）分解（MAP）执行，然后再将结果规约（REDUCE）成最终结果。

    ![](/photos/03-map-reduce.png)

    Google 2014年 I/O大会：`Google`已经停用`MapReduce`，开发并发布了一个新的超大规模云分析系统`Cloud Dataflow`。

    ![](/photos/01-aggregation-pipeline.png)

    ###MapReduce 命令

    以下是MapReduce的基本语法：
    ```javascript
    >db.collection.mapReduce(
       function() {emit(key,value);},  //map 函数
       function(key,values) {return reduceFunction},   //reduce 函数
       {
          out: collection,
          query: document,
          sort: document,
          limit: number
       }
    )
    使用 MapReduce 要实现两个函数 Map 函数和 Reduce 函数,Map 函数调用 emit(key, value), 遍历 collection 中所有的记录, 将key与 value 传递给 Reduce 函数进行处理。

    Map 函数必须调用 emit(key, value) 返回键值对。

    参数说明:

    map ：映射函数 (生成键值对序列,作为 reduce 函数参数)。
    reduce ：（规约）统计函数，reduce函数的任务就是将key-values变成key-value，也就是把values数组变成一个单一的值value。
    out ：统计结果存放集合 (不指定则使用临时集合,在客户端断开后自动删除)。
    query ：一个筛选条件，只有满足条件的文档才会调用map函数。（query，limit，sort可以随意组合）
    sort ：和limit结合的sort排序参数（也是在发往map函数前给文档排序），可以优化分组机制
    limit ：执行map函数之前，限定文档数量的上限（要是没有limit，单独使用sort的用处不大）
    MR示例
    现有集合 orders 内容如下

    db.orders.insert([
    {
         _id: 1,
         cust_id: "marong",
         ord_date: new Date("Oct 04, 2012"),
         status: 'A',
         items: [ { sku: "mmm", qty: 5, price: 2.5 },
                  { sku: "nnn", qty: 5, price: 2.5 } ]
    },
    {
         _id: 2,
         cust_id: "marong",
         ord_date: new Date("Oct 05, 2012"),
         status: 'B',
         items: [ { sku: "mmm", qty: 5, price: 3 },
                  { sku: "nnn", qty: 5, price: 3 } ]
    }
    ])
    计算每个客户的总消费
    执行过程：



    1. 执行 map 操作过程
    定义 map (映射) 函数来处理每个文档：
    映射每个文档的cust_id, 并处理 items
    先遍历 items，分别对每个items成员 qty和price相乘再求总和
    var mapFunction2 = function() {
                           var key = this.cust_id;
                           var value = 0;
                           for (var idx = 0; idx < this.items.length; idx++) {
                                value += this.items[idx].qty * this.items[idx].price;
                           }
                           emit(key, value);
                        };
    2. 定义reduce 函数有两个参数 keyCustId 和 valuesPrices
    valuesPrices 是数组，由 keyCustId 分组, 收集 value 而来
    reduces 函数 对 valuesPrices 数组 求和.
    var reduceFunction2 = function(keyCustId, valuesPrices) {
                         return Array.sum(valuesPrices);
                      };
    3. 执行 map-reduce 函数
    db.orders.mapReduce(
                         mapFunction2,
                         reduceFunction2,
                         { out: "map_reduce_example" }
                       )

    python交互
    点击查看官方文档
    安装python包
    进入虚拟环境
    sudo pip install pymongo
    或源码安装
    python setup.py
    引入包pymongo
    import pymongo
    连接，创建客户端
    client=pymongo.MongoClient("localhost", 27017)
    获得数据库test1
    db=client.test1
    获得集合stu
    stu = db.stu
    添加文档
    s1={name:'gj',age:18}
    s1_id = stu.insert_one(s1).inserted_id
    查找一个文档
    s2=stu.find_one()
    查找多个文档1
    for cur in stu.find():
        print cur
    查找多个文档2
    cur=stu.find()
    cur.next()
    cur.next()
    cur.next()
    获取文档个数
    print stu.count()
'''





