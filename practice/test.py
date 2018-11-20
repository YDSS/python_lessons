#coding=utf-8

param1 = 1
param2 = [1, 2, 3]

def testParam(num, arr):
    num += 1
    arr[0] += 1

testParam(param1, param2)

print param1
print param2