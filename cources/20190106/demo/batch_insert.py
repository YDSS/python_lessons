# coding=utf-8

import db_info
import MySQLdb
import time
import csv

# 获取数据库对象
db = MySQLdb.connect(host=db_info.host, user=db_info.user, db=db_info.db_name, charset='utf8')
# 获取数据库游标
cursor = db.cursor()
# 插入的条数
total = 0

def readRows(path, total, fn):
    "按行读取csv文件的内容，传给fn"
    with open(path, "r") as f:
        reader = csv.reader(f)
        index = 0

        for row in reader:
            if index == total:
                return
            
            date = row[0]
            time = row[1]
            num = row[2]

            apply(fn, (time, date, num))
            
            index += 1

def insertRowAndCommit(*args):
    "向数据库里插入一条数据，然后直接提交事务"
    sql = """
    insert into data_min values('%s', '%s', '%s') 
    """ % (args[0], args[1], args[2])

    try:
        cursor.execute(sql)
        db.commit()
        # total += cursor.rowcount
    except Exception, Argument:
        # 打印报错信息
        print Argument
        # 回滚事务
        db.rollback()

def getTotalCount():
    "获取数据库的总条数"
    cursor.execute('select count(1) from data_min')
    return cursor.fetchone()[0]

# 计算插入总共耗费的时间
now = time.time()
readRows("data.csv", 10, insertRowAndCommit)
cost = time.time() - now

# print "insert %d rows totally" % total
print "cost %fs" % (cost / 1000)

db.close()