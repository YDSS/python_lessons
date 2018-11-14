# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:56:21 2018

@author: Administrator
"""

def list_del(a):
    for i in a:
        if a.count(i)>1:
            a.remove(i);
    print a
       
a=[2,3,4,5,5,6];
list_del(a)