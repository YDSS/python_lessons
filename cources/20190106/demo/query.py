#coding=utf-8

import db_info
import MySQLdb

# 获取数据库对象
db = MySQLdb.connect(host=db_info.host, user=db_info.user, db=db_info.db_name, charset='utf8')
# 获取数据库游标
cursor = db.cursor()
# 执行sql语句
cursor.execute('SELECT * from data_min')
data = cursor.fetchone()
# 查询表总条数
cursor.execute('select count(1) from data_min')
count = cursor.fetchone()

print 'data from test: id(%s), desc(%s), status(%f)' % (str(data[0]), str(data[1]), data[2])
print 'total: %d' % count[0]

db.close() # 使用完数据库之后，要关闭连接