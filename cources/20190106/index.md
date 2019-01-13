# python与数据库

1. 数据库部分
    1. 数据库server架构图
    2. 使用phpMyAdmin可视化管理数据库
    3. 数据库基础语法
        1. 变量类型
        2. 添加用户、授权
            1. 给用户授权
                `grant select on 数据库.* to 用户名@登录主机 identified by “密码”`
            2. 添加用户

                `CREATE USER 'username'@'host' IDENTIFIED BY 'password'`
        3. 表的增删改查
            1. 创建表

                `create table <表名> ( <字段名1> <类型1> [,..<字段名n> <类型n>]);`

                栗子：

                ```sql
                create table MyClass(
                 id int(4) not null primary key auto_increment,
                 name char(20) not null,
                 sex int(4) not null default '0',
                 degree double(16,2));
                ```
            2. 删除表

                `drop table <表名>`

                栗子：

                ```sql
                drop table test;
                ```
            3. 查询表数据

                `select <字段1，字段2，...> from < 表名 > where < 表达式 >`

                栗子：

                ```sql
                select * from MyClass;
                ```
            4. 向表中插入数据

                `insert into <表名> [( <字段名1>[,..<字段名n > ])] values ( 值1 )[, ( 值n )]`

                栗子：

                ```sql
                insert into MyClass values(1,'Tom',96.45),(2,'Joan',82.99), (2,'Wang', 96.59);
                ```
            5. 删除表中的数据

                `delete from 表名 where 表达式`

                栗子：

                ```sql
                delete from MyClass where id=1;
                ```
            6. 修改表中的数据

                `update 表名 set 字段=新值,… where 条件`

                栗子：

                ```sql
                UPDATE [LOW_PRIORITY] [IGNORE] tbl_name SET col_name1=expr1 [, col_name2=expr2 ...] [WHERE where_definition] [ORDER BY ...] [LIMIT row_count]
                ```
            7. 修改表中的字段

                `alter table 表名 add字段 类型 其他;`

                栗子：

                ```sql
                alter table MyClass add passtest int(4) default '0'
                ```
        4. 数据库的增删
            1. 创建数据库

                `create database <数据库名>`
            2. 显示现有数据库

                `show databases`
            3.  删除某个数据库

                `drop database <数据库名drop database <数据库名>>`
            4. 连接数据库

                `use <数据库名>`
    4. 存储过程（简单介绍）
2. 使用python操作数据库
    1. 使用mysql-connector-python or MySQLdb
        1. 安装 [https://www.codegood.com/archives/129](https://www.codegood.com/archives/129) 下载对应bit的exe文件，安装即可

            api文档：http://mysql-python.sourceforge.net/MySQLdb.html#functions-and-attributes
        1. 连接数据库
        2. 查找数据
        3. 修改数据
        4. 批量处理数据
            1. 批量插入数据
                1. 单条insert，1000条数据耗时51s
                2. 单次1000条insert，1000条数据耗时.153s
    2. 使用orm框架
        1. 什么是orm
        2. orm的好处
        3. 如何使用SQLAlchemy
3. 作业
    1. 写一个脚本，把csv文件里的数据导入到数据库
    2. 写一个脚本，把数据库里的数据导出到一个csv文件里