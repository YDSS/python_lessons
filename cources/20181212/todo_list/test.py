#coding=utf-8

from utils import *

def funcA(fn):
    print 'exec func a'
    apply(fn, ('123', '456'))

def funcB(arg1, arg2):
    print 'exec func b'
    print arg1, arg2

    def inner():
        print "inner"
    
    inner()

# funcA(funcB)
# funcB()

printSeparator(funcB, '123', '456')