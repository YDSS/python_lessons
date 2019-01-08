# coding=utf-8

import db_info
import MySQLdb
import time

# 获取数据库对象
db = MySQLdb.connect(host=db_info.host, user=db_info.user, db=db_info.db_name, charset='utf8')
# 获取数据库游标
cursor = db.cursor()

# 获取当前的条数
cursor.execute('select count(1) from data_min')
count = cursor.fetchone()[0]

now = time.localtime()
now_datetime = time.strftime("%Y-%m-%d %H:%M:%S", now)
now_date = time.strftime("%Y-%m-%d", now)

# 向数据库里插入一条数据
cursor.execute("""
insert into data_min values('%s', '%s', %f) 
""" % (now_date, now_datetime, .5)
)

# 获取当前的条数
cursor.execute('select count(1) from data_min')
count_now = cursor.fetchone()[0]

print "before count: %d, now count: %d" % (count, count_now)

db.close()