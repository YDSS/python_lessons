#coding=utf-8

import Todo

class TodoList():
    __list # 存放所有的todo项
    
    def __init__(self):
        self.__list = {}
        
    def add(self, desc):
        "新增一个todo项"
        todo = Todo(desc) # 创建一个新的todo项实例
        id = todo.getId()
        
        self.__list[id] = todo

        return todo
    
    def delete(self, id):
        "移除一个todo项"
        if not self.__list.has_key(id): # 若id不存在于list中，返回false
            return False

        todo = self.__list[id]
        del self.__list[id]

        return todo

    def complete(self, id):
        "将列表中的一个todo项置成完成状态" 
        if not self.__list.has_key(id): # 若id不存在于list中，返回false
            return False
        
        todo = self.__list[id]
        todo.complete()

        return True

    def show(self):
        "把列表中所有的todo项以字符串的形式返回"
        ret = ""

        for todo in self.__list:
            ret += todo.toString()
            ret += "\n" # 换行符

        return ret