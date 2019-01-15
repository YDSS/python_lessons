#coding=utf-8

import db_info
# import MySQLdb
import mysql.connector

# 获取数据库对象
# db = MySQLdb.connect(host=db_info.host, user=db_info.user, db=db_info.db_name, charset='utf8')
db = mysql.connector.connect(host=db_info.host, user=db_info.user, password=db_info.passwd, database=db_info.db_name)
# 获取数据库游标
cursor = db.cursor()
# 执行sql语句
cursor.execute('SELECT * from data_min')
data = cursor.fetchone()
# 查询插入的条数
count = cursor.rowcount
# 查询总条数
# cursor.execute('select count(1) from data_min')
# total = cursor.fetchone()

print 'data from data_min: id(%d), date(%s), time(%s), num(%f)' % (data[3], str(data[0]), str(data[1]), data[2])
print 'insert: %d rows' % count
# print 'total: %d rows' % total

db.close() # 使用完数据库之后，要关闭连接