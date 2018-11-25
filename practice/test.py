# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Person(object):
    __id = '1234567' # 私有变量
    ancestor = 'ape' # 静态变量

    def __init__(self, name, age, gender):
        self.name = name # 成员变量
        self.age = age
        self.gender = gender
    
    def getId(self):
        return self.__id[0:3] + '**' + self.__id[5:]

    # 静态方法
    @staticmethod
    def getClassName():
        return "Person"

    # 成员方法
    def talk(self, words):
        print "%s said: %s" % (self.name, words)

    # 私有方法
    def __privateFunc(self):
        print "test"

    # 使用私有方法 
    def usePrivate(self):
        self.__privateFunc()

p = Person('pp', 23, 'male')
print p.getId()
# print Person.getClassName() # Person
# p.usePrivate() # test
# p.__privateFunc() # 报错


# # print p.__wxNum
# # print p.phoneNum
# # Person.talk('1')
# print Person.getClassName()

# class Person(object):
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def __del__(self):
#         print "%s 被销毁了" % self.name 
#     def talk(self, words):
#         print "%s said: %s" % (self.name, words)

# witch = Person('小魔女', 7, '不知道')
# print witch.age
# witch.talk('哦')
