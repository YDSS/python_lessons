# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 多多接球游戏，面向对象思想实现

class Master():
    "主人"
    def __init__(self, name):
        self.name = name 

    def pickBall(self):
        print "%s 捡起了一个球" % self.name

    def getAttention(self, dog):
        dog.gotAttentions(self.name)
    
    def throwBall(self):
        print "%s 抛出了一个球" % self.name

class Dog():
    "狗"
    def __init__(self, name):
        self.name = name

    def gotAttentions(self, name):
        print "%s 引起了 %s 的注意" % (name, self.name)
    
    def pickBallAndBack(self):
        print "%s 捡回了抛出去的球" % self.name

def startGame():
    master = Master('小魔女')
    dog = Dog('多多')

    master.pickBall()
    master.getAttention(dog)
    master.throwBall()
    dog.pickBallAndBack()

startGame()