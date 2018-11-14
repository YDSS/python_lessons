# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:56:21 2018

@author: Administrator
"""

"""
问题：

1. 函数名要代表这个函数的功能，是一个动词。这个函数是删除list里的重复元素
"""

def uniq_list_v1(a):
    "删除重复元素"
    for i in a:
        if a.count(i) > 1:
            # 回答你第一个问题，为什么a = a.remove(i)会报错
            #  list.remove(i)这个函数，没有返回值，在你第一次赋值给a的时候，a就变成空值了，在下一次进入这个循环时，因为空值没有count方法，就会报错了
            #  要学会看报错信息亲爱的：
            #    AttributeError: 'NoneType' object has no attribute 'count'
            a.remove(i) 
    print a

a = [2, 3, 4, 5, 5, 6, 2, 35, 2]
# uniq_list_v1(a)

# 第二个问题，list.count方法每次都会遍历整个list，设list有n个元素，uniq_list_v1就要执行最 n*n 次 http://www.runoob.com/python/att-list-count.html
# remove方法会a的第一个元素开始查找，删除第一个和i相等的元素然后删除它，这样 也需要执行 n*n 次 http://www.runoob.com/python/att-list-remove.html

# 改进版，只需要执行最多 n 次
def uniq_list_v2(a):
    "删除重复元素"
    # 定义一张记录重复数据的空表，
    map = {}
    # 新列表
    ret = []
    # 这里使用索引值取a中的元素，因为删除元素需要用到索引值
    for index in range(len(a) - 1):
        element = a[index]
        key = str(element)

        if (not map.has_key(key)):
            # 这里可以是任意为None的值，相当于标记
            map[key] = True
            # 把不重复的元素放到新列表里
            ret.append(element)
    # 返回新列表
    return ret

print uniq_list_v2(a)
