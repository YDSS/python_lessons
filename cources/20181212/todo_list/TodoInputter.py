#coding=utf-8

import Todo
import TodoList

ADD = "add"
DELETE = "delete"
COMPLETE = "complete"
SHOW = "show"
QUIT = "quit"

"""
接收用户输入的类
"""
class TodoInputter():
    
    def __init__(self):
        self.todoList = TodoList()

    def start(self):
        "开始接收用户命令"
        while True:
            command = input("please into a command: ")         

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
        desc = input("enter desc: ")
        todo = self.todoList.add(desc)        

        print todo.toString()

    def delete(self):
        "接收用户删除一个todo的命令"
        id = input("enter id: ")
        ret = self.todoList.delete(id)

        if not ret:
            print "id not found! try again"            
            self.delete()
        else:
            print todo.toString()

    def complete(self):
        "接收用户将一个todo项设置成完成状态的命令"
        id = input("enter id: ")
        ret = self.todoList.complete(id)

        if not ret:
            print "id not found! try again"            
            self.complete()
        else:
            print todo.toString()

    def show(self):
        "接收用户显示所有todo项的命令" 
        self.todoList.show()