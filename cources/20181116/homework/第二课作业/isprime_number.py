# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:39:53 2018

@author: lenovo
"""
def isprime_number(x):
    if x <2:
        print "请输入大于1的自然数";###判断输入的数是不是大于1
    elif int(x) - x != 0:####判断输入的数是不是自然数
        print "请输入自然数";
    elif x % 2 == 0 or x % 3 == 0:
        print "该数不为素数";
    else:
        print "该数为素数"
isprime_number(25) # 25不是质数

# 如果要求传入值向后最近的一个质数?