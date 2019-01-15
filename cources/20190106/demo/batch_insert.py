# coding=utf-8

import db_info
import MySQLdb
import time
import csv
import math
import pandas

# 获取数据库对象
db = MySQLdb.connect(host=db_info.host, user=db_info.user, db=db_info.db_name, charset='utf8')
# 获取数据库游标
cursor = db.cursor()
# 插入的条数
total = 0

def readRowsAndCallback(path, total, fn):
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

def readRowsOnceATime(path, total, fn):
    "按行读取csv文件的内容，传给fn"
    rows = []
    with open(path, "r") as f:
        reader = csv.reader(f)
        index = 0

        for row in reader:
            if index == total:
                break 
            
            rows.append(row)
            index += 1

    apply(fn, (rows,))

def readRowsOnceATimeEnhance(path, interval, fn):
    "用pandas读取csv文件的内容，每次读取interval行,传给fn"
    

    apply(fn, (rows,))

def insertRowOnceATime(*args):
    "每次向数据库里插入一条数据，然后直接提交事务"
    sql = """
    insert into data_min values('%s', '%s', '%s') 
    """ % (args[0], args[1], args[2])

    try:
        cursor.execute(sql)
        db.commit()
    except Exception, Argument:
        # 打印报错信息
        print Argument
        # 回滚事务
        db.rollback()

def insertRowOnceATime(*args):
    "每次向数据库里插入10000条数据，然后提交事务"
    rows = args[0]
    i = 0
    buff_len = 10000
    rows_len = len(rows)
    sql = "insert into data_min values"

    try:
        while i <= rows_len:
            end = i + buff_len
            if rows_len - end < 0:
                end = rows_len - i

            values = ""
            for j in range(i, end):
                row = rows[j]
                values += ("('%s', '%s', %f)," % (row[0], row[1], float(row[2])))

            values = values[0: len(values) - 1]
            cursor.execute(sql + values)
            db.commit()
            print "inset %d rows" % cursor.rowcount

            i += buff_len

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
# readRowsAndCallback("data.csv", 1000, insertRowOnceATime)
readRowsOnceATime("data.csv", 100000, insertRowOnceATime)
cost = time.time() - now

# print "insert %d rows totally" % total
print "cost %fs" % cost

db.close()