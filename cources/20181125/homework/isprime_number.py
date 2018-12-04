# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:39:53 2018

@author: lenovo
"""

def isprime_number(x):
    if x < 2:
        print "请输入大于1的自然数";###判断输入的数是不是大于1
    elif int(x) - x != 0:####判断输入的数是不是自然数
        print "请输入自然数";
    elif x == 2:
         print '该数为素数'
    elif x > 2:
        if x >= 10:
            list = range(2,10,1);
        else:
            list = range(2,x,1);
        for i in list:
            if x % i == 0:
                break; 
        if i == list[-1]:
            print '该数为素数'
        else:
            print '该数不是素数'
            
                
   
        
isprime_number(4.1)