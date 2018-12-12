#coding=utf-8

"""
待办项类
"""
import time
import utils

class Todo():
    baseId = 0
    __id = 0 # todo项的id，唯一，且不能修改
    """
    todo项的状态，0表示未完成，1表示已完成，外界只能通过complete方法修改
    """
    __status = 0 # 待办项初始化时默认为未完成

    def __init__(self, desc=""):
        self.__id = self.__createTodoId()
        self.desc = desc
        self.createTime = utils.getCurrentTime()

    def getId(self):
        "获取todo的id"
        return self.__id

    def __createTodoId(self):
        tmp = Todo.baseId
        Todo.baseId += 1

        return tmp
    
    def complete(self):
        "将todo设置成完成状态"
        self.__status = 1
        self.completeTime = utils.getCurrentTime()

    def isComplete(self):
        "该todo项是否已完成"
        return self.__status == 1
    
    def toString(self):
        string = "id: " + str(self.__id) + " ,描述: " + self.desc + ", 创建时间: " + self.createTime + ", 是否已完成: " + str(self.isComplete())
        if self.isComplete():
                string += (", 完成时间: " + self.completeTime)
        
        return string