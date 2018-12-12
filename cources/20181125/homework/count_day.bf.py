# -*- coding: utf-8 -*-
"""
思考题：

1. 根据天数求日期，比如 2018年的第76天 是 2018.3.16
"""

def count_day(Y,M,D):
    if Y % 400 ==0 or (Y % 4 == 0 and Y % 100 != 0):###闰年
        list_days=[31,29,31,30,31,30,31,31,30,31,30,31];
    else:
        list_days=[31,28,31,30,31,30,31,31,30,31,30,31];
    if M > 12 or M < 1 or list_days[M-1] < D or list_days[M-1] < D or D < 1:
        print '请输入正确的月份'
    else:
        days1 = 0;
        for i in range(0,M,1):
            if i == M-1:
                break;
            days1 += list_days[i]; 
        days = days1 + D;
        return days
    
print count_day(2018, -1, 30) 