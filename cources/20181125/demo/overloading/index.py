# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def talk(self, words):
        print "%s said: %s" % (self.name, words)
    
class Student(Person):
    def __init__(self, name, age, gender, grade):
        parent = super(Student, self)
        print parent
        parent.__init__(name, age, gender)

        self.grade = grade

    def talk(self, words):
        "方法重写"
        print "I'm %s" % self.name
        super(Student, self).talk(words)

    def talk(self, *words):
        "方法重载"
        print "这是方法重载"
        for word in words:
            print word

s = Student('s', 23, 'female', 5)
s.talk('hahaha')
s.talk('1', '2', '3')