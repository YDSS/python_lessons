#coding=utf-8

from Todo import *
from TodoList import *
from utils import *

ADD = "add"
DELETE = "delete"
COMPLETE = "complete"
SHOW = "show"
QUIT = "quit"

"""
接收用户输入的类
"""
class TodoInputter():
    
    def __init__(self, list=None):
        self.todoList = list or TodoList()

    def start(self):
        "开始接收用户命令"
        while True:
            command = raw_input("please into a command: ")         

            if command == ADD:
                self.add()
            elif command == DELETE:
                self.delete()
            elif command == COMPLETE:
                self.complete()
            elif command == SHOW:
                self.show()
            elif command == QUIT:
                break
            else:
                print "command not corrent! try again"
    
    def add(self):
        "接收用户添加todo的命令"
        desc = raw_input("enter desc: ")
        todo = self.todoList.add(desc)        
        
        utils.printSeparator(TodoInputter.printOpInfo, todo, "added a new todo:")

    def delete(self):
        "接收用户删除一个todo的命令"
        id = utils.inputInt("enter id: ")

        todo = self.todoList.delete(id)

        if not todo: # 这里todo是boolean
            print "id not found! try again"            
            self.delete()
        else:
            utils.printSeparator(TodoInputter.printOpInfo, todo, "deleted a todo:")

    def complete(self):
        "接收用户将一个todo项设置成完成状态的命令"
        id = utils.inputInt("enter id: ")
        todo = self.todoList.complete(id)

        if not todo: # 这里todo是boolean
            print "id not found! try again"            
            self.complete()
        else:
            utils.printSeparator(TodoInputter.printOpInfo, todo, "this todo is completed:")

    def show(self):
        "接收用户显示所有todo项的命令" 
        def showTodolist():
            print self.todoList.show()

        utils.printSeparator(showTodolist)

    @staticmethod
    def printOpInfo(todo, tip):
        "打印命令执行完成后的结果"
        print tip
        print todo.toString()