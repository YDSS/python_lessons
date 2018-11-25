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

class PickGame():
    def __init__(self, master, dog):
        self.master = master
        self.dog = dog
            
    def startGame(self):
        self.master.pickBall()
        self.master.getAttention(self.dog)
        self.master.throwBall()
        self.dog.pickBallAndBack()

    def __del__(self):
        self.master = None
        self.dog = None
        print "执行析构函数"

master = Master('a')
dog = Dog('b')
game = PickGame(master, dog)

game.startGame()
del game