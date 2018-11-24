# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Person(object):
    __wxNum = 1234567
    phoneNum = 1232131313

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def talk(self, words):
        print "%s said: %s" % (self.name, words)

    @staticmethod
    def getClassName():
        return "Person"

p = Person('ppp', 23, 'male')

# print p.__wxNum
# print p.phoneNum
# Person.talk('1')
print Person.getClassName()
