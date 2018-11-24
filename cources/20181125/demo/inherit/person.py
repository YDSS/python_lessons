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
    
# p1 = Person('arlen', 27, 'male')
# p1.talk('happy')

class Student(Person):
    def __init__(self, name, age, gender, grade):
        parent = super(Student, self)
        print parent
        parent.__init__(name, age, gender)

        self.grade = grade

s = Student('s', 23, 'female', 5)
for attr in s.__dict__:
    print attr