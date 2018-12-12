# encoding=utf-8
"""
@author: arlenyang
"""

"""
还是不对哟，亲爱的。
你只判断了一个数是否可以被10以内的数整除，如果是10以上的质数的平方依旧检测不到，比如 11*11 = 121
实际上上次举的反例是质数的幂次方，还有其他的情形，比如两个质数的乘积

思路：所以不能用简单的列举法来判断一个质数，实际上质数序列是一个无限且出现规律不明（现在仍然没有公式能算出质数的出现规律）的序列，判断一个数是否
为质数，只能通过除以该数字与1之间的所有自然数，如果都不被整除，则它是质数

语法问题：
1. 写一个方法，最好把结果通过 return 返回，而不是print出来，这样它还可以用在其他地方做计算
2. ;可以省略，更简洁美观
3. 异常处理最好用exception

思考题（必做）：
1. 下面的实现还可以再优化，从性能的角度，看看如何减少计算的次数
2. 求与输入数字最接近的、比它大的质数
"""
def isPrime(x):
    if x < 2:
        raise Exception("must gt 1") # 判断输入的数是不是大于1
    elif int(x) - x != 0: # 判断输入的数是不是自然数
        raise Exception("must be a natural number")
    elif x > 2:
        list = range(2, x)
        flag = True # 判断该数是否为质数，初始值为真，若有整除的情况即置为False，且不用再继续循环

        for i in list:
            if x % i == 0:
                flag = False 
                break

        return flag
            
num = input('please input a natural number:')
print isPrime(num)