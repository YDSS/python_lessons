# coding=utf-8

import db_info
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

try:
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://%s:%s@%s:3306/%s' % (db_info.user, db_info.passwd, db_info.host, db_info.db_name))
    # 创建DBSession类型:
    session = sessionmaker(bind=engine)
    print session
except Exception, Argument:
    print Argument