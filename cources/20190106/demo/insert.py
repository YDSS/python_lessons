# coding=utf-8

import db_info
import mysql.connector
import time

# 获取数据库对象
db = mysql.connector.connect(host=db_info.host, user=db_info.user, password=db_info.passwd, database=db_info.db_name)
# 获取数据库游标
cursor = db.cursor()

now = time.localtime()
now_datetime = time.strftime("%Y-%m-%d %H:%M:%S", now)
now_date = time.strftime("%Y-%m-%d", now)

sql = """
    insert into data_min(date, time, num) values('%s', '%s', %f) 
    """ % (now_date, now_datetime, .5)

print sql

# 向数据库里插入一条数据
try:
    cursor.execute(sql)
    db.commit()
    # 获取插入的条数
    print "insert %d row" % cursor.rowcount
except Exception, Argument:
    print Argument 
    # rollback
    db.rollback()

db.close()