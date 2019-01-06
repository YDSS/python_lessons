#coding=utf-8

"""
工具模块，提供一些常用的方法
"""

import time

def getCurrentTime():
    "获取当前时间"
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

def printSeparator(fn, *args):
    "在fn执行的前后打印分隔符，把每次的显示结果分隔开，方便查看"
    print '-----------------------------'
    apply(fn, args)    
    print '-----------------------------'

def inputInt(tip):
    "python2的input会把int输入转成字符串，这里转回来"
    s = input(tip)

    return int(s)