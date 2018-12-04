# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:17:15 2018

@author: xiaobai
"""

def count_day(Y,M,D):
    if Y % 400 ==0 or (Y % 4 == 0 and Y % 100 != 0):###闰年
        list_days=[31,29,31,30,31,30,31,31,30,31,30,31];
    else:
        list_days=[31,28,31,30,31,30,31,31,30,31,30,31];
    if M > 12 or list_days[M-1] < D:
        print '请输入正确的月份'
    else:
        days1 = 0;
        for i in range(0,M,1):
            if i == M-1:
                break;
            days1 += list_days[i]; 
        days = days1 + D;
        return days
    
 