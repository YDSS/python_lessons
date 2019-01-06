#coding=utf-8

import csv
from Todo import Todo
from TodoList import TodoList

"""
存储todo数据的类
"""
class TodoStore():

    __list = {}

    def __init__(self, csvPath):
        self.csvPath = csvPath
        self.__list = self.__readCsv(csvPath)
    
    def __readCsv(self):
        "一次读取所有csv文件里的todo数据，并转换成todolist"
        todoDict = {} # 存放所有已存在的todo项

        with open(self.csvPath, "r") as f: # 打开文件的方式，看这里http://www.runoob.com/python/python-func-open.html
            reader = csv.reader(f)
            # header = next(reader) # 跳过第一行，标题栏
            
            for row in reader:
                # 遍历每行的数据
                id = row[0]
                desc = row[1]
                status = row[2]
                createTime = row[3]
                completeTime = row[4]

                todo = Todo(id=id, desc=desc, status=status, createTime=createTime, completeTime=completeTime)                    
                todoDict[id] = todo
        
        return TodoList(list=todoDict)
    
    def addTodo(self, todo):
        "添加一条todo数据，同时存入csv"
        if (todo.isComplete()):
            status = 1
        else:
            status = 0
        row = [todo.getId(), todo.desc, status, todo.createTime, todo.completeTime]

        with open(self.csvPath, 'a') as f: # 以追加的方式（a）打开文件，向文件结尾添加一行
            writer = csv.writer(f)
            writer.writerow(row) 
            self.__list.add(todo)
        
    def delTodo(self, todo):
        "删除与传入的todo匹配的数据，同时删除"
        id = todo.getId()
        