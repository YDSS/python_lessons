# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:13:45 2018

@author: xiaobai aiyaya
"""

def count_day(Y,M,D):
    list_days=[31,28,31,30,31,30,31,31,30,31,30,31];
    if Y % 400 ==0 or (Y % 4 == 0 and Y % 100 != 0):
        list_days[1] += 1

    days1 = 0;
    for i in range(0,M,1):
        if i == M-1:
            break;
        days1 += list_days[i];        
    days=days1+D;
    return days

print count_day(2018,12,34) # 哦豁       
