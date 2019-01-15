# coding=utf-8

import db_info
# import MySQLdb
import mysql.connector

# 获取数据库对象
# db = MySQLdb.connect(host=db_info.host, user=db_info.user, db=db_info.db_name, charset='utf8')
db = mysql.connector.connect(host=db_info.host, user=db_info.user, password=db_info.passwd, database=db_info.db_name)
# 获取数据库游标
cursor = db.cursor()

# 更新id=1的数据
sql = "update data_min set num=0.1 where id = 2"
try:
    cursor.execute(sql)
    db.commit()
except Exception, Argument:
    print Argument
    db.rollback()

db.close()