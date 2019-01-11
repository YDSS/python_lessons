# coding=utf-8

import db_info
from sqlalchemy import Column, Date, DateTime, Float, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DateMin(Base):
    __tablename__ = 'data_min'
    date = Column(Date())
    time = Column(DateTime())
    num = Column(Float())

try:
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://%s:%s@%s:3306/%s' % (db_info.user, db_info.passwd, db_info.host, db_info.db_name))
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    data = DateMin(date = "2019-01-12", time = "2019-01-12 11:22:00", num = 0.12355)
    session.add(data)
    session.commit()
    session.close()
except Exception, Argument:
    print Argument
