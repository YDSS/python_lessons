# -*- coding: utf-8 -*-
"""
@file implementation of fibonacci sequence
@author: arlenyang
@date: 2018-11-13
"""

"""
问题：
1. 表达式语句前后的变量分开更美观 n == 1 而不是 n==1
2. 函数要有注释，至少可以写一下函数文档注释
3. 如果输入是0 或者小于 0，怎么处理？要考虑异常处理
"""

def f(n):
    "斐波那契数列实现"
    if n <= 0: # 异常处理逻辑 
        raise RuntimeError("斐波那契数列从1开始，请重新输入")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)

n = input("请输入一个数:") 
for i in range(1, n + 1, 1):
    print f(i)

