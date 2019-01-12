# coding=utf-8

import db_info
from sqlalchemy import Column, Date, DateTime, Float, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
session

class DateMin(Base):
    "data_min表的orm映射"
    __tablename__ = 'data_min'
    id = Column(Integer, primary_key=True)
    date = Column(Date())
    time = Column(DateTime())
    num = Column(Float())

try:
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://%s:%s@%s:3306/%s' % (db_info.user, db_info.passwd, db_info.host, db_info.db_name))
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建一个session
    session = DBSession()
    # 创建一条记录
    data = DateMin(date = "2019-01-12", time = "2019-01-12 11:22:00", num = 0.12355)
    session.add(data)
    session.commit()
    session.close()
except Exception, Argument:
    print Argument
