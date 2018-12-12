#coding=utf-8

"""
工具模块，提供一些常用的方法
"""

import time

id = 0

def createTodoId():
    "生成todo项的id"
    curId = id
    id += 1

    return curId

def getCurrentTime():
    "获取当前时间"
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())