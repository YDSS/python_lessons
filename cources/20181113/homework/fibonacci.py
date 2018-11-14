# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:07:28 2018

@author: Administrator
"""

def f(n):
    if n==1:
        return 1;
    elif n==2:
        return 1;
    else:
        return f(n-1)+f(n-2);

n=input("请输入一个数:")  7           
for i in range(1,n+1,1):
    print f(i)
