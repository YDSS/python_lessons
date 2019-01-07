#coding=utf-8

import MySQLdb

# 数据库相关配置信息
host = 'localhost' # 数据库ip
user = 'root' # 用户名
passwd = '' # 密码
db_name = 'mysql' # 数据库名

# 获取数据库对象
db = MySQLdb.connect(host=host, user=user, db=db_name, charset='utf8')
# 获取数据库游标
cursor = db.cursor()
# 执行sql语句
cursor.execute('SELECT * from test')
data = cursor.fetchone()

print 'data from test: id(%d), desc(%s), status(%d)' % (data[0], data[1], data[2])

db.close()