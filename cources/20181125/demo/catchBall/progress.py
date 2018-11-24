# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 多多接球游戏，面向过程思想实现

def pickBall(master):
    "捡球"
    print "%s 捡起了一个球" % master

def getAttention(master, dog):
    "引起狗的注意，不然即使抛了球也可能不理你"
    print "%s 引起了 %s 的注意" % (master, dog)

def throwBall(master):
    "抛球"
    print "%s 抛出了一个球" % master

def pickBallAndBack(dog):
    "捡球"
    print "%s 捡回了抛出去的球" % dog

def startGame(master, dog):
    pickBall(master)
    getAttention(master, dog)
    throwBall(master)
    pickBallAndBack(dog)

startGame(master="小魔女", dog="多多")