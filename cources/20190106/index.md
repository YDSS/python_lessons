# 搭建Mysql及数据库可视化工具

## 安装xampp安装包

[https://www.apachefriends.org/index.html](https://www.apachefriends.org/index.html)

## 使用phpMyAdmin

1. 执行安装包
2. 打开可视化工具的控制台。先找到安装xampp的位置，里面有一个`xampp-control.exe`的文件，双击就可以打开控制台

    ![img](F:\private\lesson\python_lessson_for_gf\python_lessons\cources\20190106\img\controll.png)

3. 打开控制台之后，**start** `Apache`和`MySQL`服务，就是点击右侧的`start`按钮（打开之后，`start`会变成`stop`，再点它就关闭了）

    ![img](F:\private\lesson\python_lessson_for_gf\python_lessons\cources\20190106\img\controll-panel.png)

4. 打开3中的两个服务之后，点击Mysql的admin按钮，就可以在页面上操作数据库啦

    ![img](F:\private\lesson\python_lessson_for_gf\python_lessons\cources\20190106\img\web-start.png)

    ![img](F:\private\lesson\python_lessson_for_gf\python_lessons\cources\20190106\img\web-panel.png)

## 操作数据库

操作数据库的方式有两种，1是通过命令行(cmd)输入sql指令，2是使用可视化工具如phpMyAdmin以**填表**的形式操作，2更方便一些。

我们先看看phpMyAdmin提供的控制台的界面：

![img](F:\private\lesson\python_lessson_for_gf\python_lessons\cources\20190106\img\interface.png)

数据库里有两层结构，最底层是各种**表**，表就类似于一个`excel`，有很多字段，每行是一条数据。上层也叫**数据库**，但它其实就是表的**集合**。

### 创建表

我们可以选择在已有的数据库里创建表，也可以自己创建一个数据库，再在里面创建表。

![img](F:\private\lesson\python_lessson_for_gf\python_lessons\cources\20190106\img\createtable.png)

填好之后点**执行**按钮就可以了。对应的创建表的SQL语法如下：

```sql
create table <表名> ( <字段名1> <类型1> [,..<字段名n> <类型n>]);
```

比如：

```sql
create table MyClass(
    id int(4) not null primary key auto_increment,
    name char(20) not null,
    sex int(4) not null default '0',
    degree double(16,2)
);
```

**可视化工具把我们在页面上填的东西拼成了上面这句sql，然后执行，和直接执行上面的sql语句是一个效果**

### 查询表

![img](F:\private\lesson\python_lessson_for_gf\python_lessons\cources\20190106\img\selecttable.png)

对应的sql语法：

```sql
select <字段1，字段2，...> from < 表名 > where < 表达式 >
```

例如上面用的查询语句：

```sql
SELECT * FROM `test`
```

__*__是通配符，表示把这个表里所有的字段都列出来，如果只想要其中的几个字段，可以这么写：

```sql
SELECT id, xx, xxx FROM `test`
```

每个字段用`,`分隔

### 导入、导出数据

phpMyAdmin支持导入、导出数据，可以把`csv`文件导入到一个表里，只要字段对应没问题就可以

![img](F:\private\lesson\python_lessson_for_gf\python_lessons\cources\20190106\img\import.png)

导出同理

### 完整的SQL语法教程

[http://www.runoob.com/mysql/mysql-tutorial.html](http://www.runoob.com/mysql/mysql-tutorial.html)